from inspect_ai import Task, task

from gage_inspect.scorer import match
from gage_inspect.solver import task_doc


@task
def add():
    """Add two numbers.

    Input:
        x: Value of x
        y: Value of y

    Output:
        Sum of x and y
    """
    return Task(
        solver=task_doc(),
        scorer=match(numeric=True),
    )
