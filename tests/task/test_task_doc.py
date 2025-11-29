from gage_inspect.task import parse_task_doc
from inspect_ai import Task, task


@task
def add() -> Task:
    """Task that adds two numbers.

    Input:
      x (int): Value for x
      y (int): Value for y

    Output:
      int: Sum of x and y

    """
    return Task()


def test_add_task_doc():
    doc = parse_task_doc(add.__doc__ or "")

    assert doc.short_description == "Task that adds two numbers."
    assert doc.long_description is None

    assert len(doc.params) == 2

    p1 = doc.params[0]
    assert p1.arg_name == "x"
    assert p1.type_name == "int"
    assert p1.description == "Value for x"

    p2 = doc.params[1]
    assert p2.arg_name == "y"
    assert p2.type_name == "int"
    assert p2.description == "Value for y"

    assert doc.returns
    assert doc.returns.description == "Sum of x and y"
    assert doc.returns.return_name is None
    assert doc.returns.type_name == "int"


@task
def math() -> Task:
    """Solve a math problem.

    Input:
      str: A math problem

    Output:
      A result

    """
    return Task()


def test_math_task_doc():
    doc = parse_task_doc(math.__doc__ or "")

    assert len(doc.params) == 1
    p1 = doc.params[0]
    assert p1.arg_name == "str"
    assert p1.type_name is None
    assert p1.description == "A math problem"

    assert doc.returns
    assert doc.returns.description == "A result"
    assert doc.returns.return_name is None
    assert doc.returns.type_name is None
