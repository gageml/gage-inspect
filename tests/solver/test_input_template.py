from yaml.parser import ParserError
from inspect_ai import Task
from pydantic import BaseModel, ValidationError
from pytest import raises

from gage_inspect.solver import input_template
from gage_inspect.solver._template import Template, input_vars
from gage_inspect.task import run_task


def test_template_basic():
    t = Template("Hello")
    assert t.render() == "Hello"

    # Empty field name uses `input` var
    t = Template("Hello {}")
    assert t.render() == "Hello "
    assert t.render({"": "xxx"}) == "Hello "
    assert t.render({"input": "Joe"}) == "Hello Joe"


def test_template_field_names():
    assert Template("").field_names() == set()
    assert Template("a").field_names() == set()
    assert Template("{a}").field_names() == {"a"}
    assert Template("{a.b.c}").field_names() == {"a.b.c"}
    assert Template("{a} {b} {c}").field_names() == {"a", "b", "c"}

    # Name list is unique
    assert Template("{a} {a}").field_names() == {"a"}
    assert Template("{a} {b} {a}").field_names() == {"a", "b"}

    # Name list is sorted
    assert Template("{c} {b} {a}").field_names() == {"a", "b", "c"}

    # Empty name is coerced to 'input'
    assert Template("{}").field_names() == {"input"}
    assert Template("{} {input}").field_names() == {"input"}
    assert Template("{} {input} {}").field_names() == {"input"}


def test_template_nested():
    t = Template("{op.lhs} {op.symbol} {op.rhs} = {op.result.value} ({op.result.type})")
    assert (
        t.render(
            {
                "op": {
                    "lhs": 12,
                    "rhs": 10,
                    "symbol": "-",
                    "result": {
                        "value": 2,
                        "type": "subtract",
                    },
                }
            }
        )
        == "12 - 10 = 2 (subtract)"
    )


def test_template_positional():
    # Positional vars must be specified as field names "0", "1", etc.
    t = Template("{0} + {1} = {2}")
    assert t.render({"0": 10, "1": 20, "2": 30}) == "10 + 20 = 30"


def test_template_missing_vars():
    t = Template("x={x} y={x.y} z={x.y.z}")

    # Missing values resolve to empty string
    assert t.render() == "x= y= z="

    # Nested values that can't traverse short-circuit to their last
    # resolved value or empty string if they have no last resolved value
    assert t.render({"x": "a"}) == "x=a y=a z=a"
    assert t.render({"x": {"y": "b"}}) == "x= y=b z=b"
    assert t.render({"x": {"y": {"z": "c"}}}) == "x= y= z=c"


def test_input_vars_auto():
    def vars(input: str, template: str | None = None):
        return input_vars(input, "auto", Template(template) if template else None)

    # Without a schema, 'auto' returns input as `{"input": input}`
    assert vars("abc") == {"input": "abc"}
    assert vars("123") == {"input": "123"}
    assert vars("true") == {"input": "true"}

    # Same behavior when template contains only `input` or empty field name
    assert vars("123", "{}") == {"input": "123"}
    assert vars("123", "{input}") == {"input": "123"}

    # If template uses other field names, input is parsed as YAML
    assert vars("x: 123", "{x}") == {"_input": "x: 123", "x": 123}
    assert vars("{x: 123, y: 456}", "{x} {y}") == {
        "_input": "{x: 123, y: 456}",
        "x": 123,
        "y": 456,
    }

    # Additional field names are not included
    assert vars("x: 123", "{x} {y}") == {"_input": "x: 123", "x": 123}

    # List items are provided as zero-based keys
    assert vars("[1, 2, red, blue]", "{0} {1} {2} {3}") == {
        "0": 1,
        "1": 2,
        "2": "red",
        "3": "blue",
        "_input": "[1, 2, red, blue]",
    }

    # If the parsed YAML cannot be mapped to a dict, the parsed value is
    # included as `input`
    assert vars("123", "{x} {y}") == {"_input": "123", "input": 123}

    # Values that cannot be parsed as YAML cause an error
    with raises(ParserError) as e:
        vars("[1", "{0}")
    assert e.value.problem == "expected ',' or ']', but got '<stream end>'"


def test_input_vars_typed():
    vars = input_vars

    assert vars("123", int) == {"_input": "123", "input": 123}
    assert vars("no", bool) == {"_input": "no", "input": False}
    assert vars("[1, 2, 3]", list[int]) == {
        "_input": "[1, 2, 3]",
        "0": 1,
        "1": 2,
        "2": 3,
    }

    # Input that doesn't comply with a type is rejected
    with raises(ValidationError) as e:
        vars("asd", int)
    assert e.value.errors()[0]["msg"] == (
        "Input should be a valid integer, unable to parse string as an integer"
    )


def test_input_vars_model():
    class Op(BaseModel):
        x: int
        y: int
        op: str
        z: float | int

    def vars(input: str):
        return input_vars(input, Op)

    assert vars("{x: 1, y: 2, op: add, z: 3}") == {
        "_input": "{x: 1, y: 2, op: add, z: 3}",
        "x": 1,
        "y": 2,
        "op": "add",
        "z": 3,
    }

    # Input that cannot be validated causes an error
    with raises(ValidationError) as e:
        assert vars("{x: 1, y: cat}") == 123
    errors = e.value.errors()
    assert len(errors) == 3
    assert errors[0]["loc"] == ("y",)
    assert errors[0]["msg"] == (
        "Input should be a valid integer, unable to parse string as an integer"
    )
    assert errors[1]["loc"] == ("op",)
    assert errors[1]["msg"] == "Field required"
    assert errors[2]["loc"] == ("z",)
    assert errors[2]["msg"] == "Field required"


def test_input_template_solver():
    # Tuple/list input
    t = Task(solver=input_template("What is {0} + {1}?"))
    assert user_msg(t, "[123, 321]") == "What is 123 + 321?"

    # Struct/dict input
    t = Task(solver=input_template("What is {x} + {y}?"))
    assert user_msg(t, "{x: 321, y: 123}") == "What is 321 + 123?"

    # Typed int
    t = Task(solver=input_template("You said {input}", float))
    assert user_msg(t, "1.123") == "You said 1.123"

    # Model validated
    class User(BaseModel):
        name: str
        id: int

    t = Task(solver=input_template("{name} ({id})", User))
    assert user_msg(t, "{name: Sam, id: 112233}") == "Sam (112233)"


def user_msg(t: Task, input: str):
    resp = run_task(t, input, model="none/none")
    if resp.log.error:
        return resp.log.error
    return resp.sample.messages[0].content
