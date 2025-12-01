from inspect_ai import Task, task
from pytest import raises

from gage_inspect.solver._task_doc import task_doc, task_doc_prompt
from gage_inspect.task import run_task


@task
def description_only():
    """Reverse the letters in a word."""
    return Task()


def test_description_only():
    assert (
        task_doc_prompt(description_only(), "abc")
        == """
Perform this task:

<task_description>
Reverse the letters in a word.
</task_description>

Here are the task inputs:

<inputs>
abc
</inputs>
""".strip()
    )


@task
def runnable():
    """Do a thing."""
    return Task(solver=task_doc())


def test_runnable():
    # Run the task
    resp = run_task(runnable(), "abc", model="mockllm/model")
    assert resp.output.error is None
    assert resp.sample.messages[0].content == (
        """
Perform this task:

<task_description>
Do a thing.
</task_description>

Here are the task inputs:

<inputs>
abc
</inputs>
""".strip()
    )


@task
def input():
    """Reverse the letters in a word.

    Input:
      value: the word to reverse
    """
    return Task()


def test_input():
    assert (
        task_doc_prompt(input(), "abc")
        == """
Perform this task:

<task_description>
Reverse the letters in a word.
</task_description>

Here are the task inputs:

<inputs>
<value description="the word to reverse">abc</value>
</inputs>
""".strip()
    )


@task
def input_and_output():
    """Reverse the letters in a word.

    Input:
      value: the word to reverse

    Output:
      Reversed word
    """
    return Task()


def test_input_and_output():
    assert (
        task_doc_prompt(input_and_output(), "abc")
        == """
Perform this task:

<task_description>
Reverse the letters in a word.
</task_description>

Here are the task inputs:

<inputs>
<value description="the word to reverse">abc</value>
</inputs>

The output should conform to this description:

<output_description>
Reversed word
</output_description>

Do not explain the results. Do not include inputs or other context. Do
not apply formatting. Return only the generated output value.
""".strip()
    )


@task
def no_description():
    return Task()


def test_no_description():
    with raises(ValueError) as e:
        task_doc_prompt(no_description(), "abc")

    assert e.value.args[0] == "task_doc solver requires a docstring with a description"


@task
def multiple_inputs():
    """Subtract.

    Input:
      lhs: Left hand side of subtract operation
      rhs: Right hand side of subtract operation
    """
    return Task()


def test_multiple_inputs():
    assert (
        task_doc_prompt(multiple_inputs(), "{lhs: two mice, rhs: one mouse}")
        == """
Perform this task:

<task_description>
Subtract.
</task_description>

Here are the task inputs:

<inputs>
<lhs description="Left hand side of subtract operation">two mice</lhs>
<rhs description="Right hand side of subtract operation">one mouse</rhs>
</inputs>
""".strip()
    )

    # Inputs require value YAML/JSON input
    with raises(ValueError) as e:
        task_doc_prompt(multiple_inputs(), "[invalid inpu")

    assert e.value.args[0].startswith("input must be valid YAML/JSON")

    # Multiple inputs require a map/dict
    with raises(ValueError) as e:
        task_doc_prompt(multiple_inputs(), "123")

    assert e.value.args[0].startswith("input must be a dict/map of named values")


def test_custom_template():
    assert (
        task_doc_prompt(
            description_only(),
            "abc",
            prologue="Do a thing.",
            inputs="Use this: {}",
            output_description="Return that.",
        )
        == """
Do a thing.

Here are the task inputs:

<inputs>
abc
</inputs>

Return that.
""".strip()
    )

    assert (
        task_doc_prompt(description_only(), "abc", prologue="{x} and {y}")
        == """
{x} and {y}

Here are the task inputs:

<inputs>
abc
</inputs>
""".strip()
    )
