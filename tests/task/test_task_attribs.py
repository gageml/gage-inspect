from inspect_ai import Task, task
from inspect_ai._util.registry import (
    registry_info,
    registry_lookup,
)

from gage_inspect.patch import patch_task_description

# Need to patch Inspect to use task docstring as description
patch_task_description()


@task
def sample():
    "A sample task."
    return Task()


@task
def sample2():
    """Line 1 is description.

    Subsequent lines are not.
    """
    return Task()


def test_task_attribs():
    # sample has a single docstring line
    f = registry_lookup("task", "sample")
    assert f is sample
    attribs = registry_info(f).metadata["attribs"]
    assert sorted(attribs) == ["__doc__", "description"]
    assert attribs["description"] == "A sample task."
    assert attribs["__doc__"] == sample.__doc__

    # sample2 has multiple docstring lines - only the first is used for
    # description
    f = registry_lookup("task", "sample2")
    assert f is sample2
    attribs = registry_info(f).metadata["attribs"]
    assert sorted(attribs) == ["__doc__", "description"]
    assert attribs["description"] == "Line 1 is description."
    assert attribs["__doc__"] == sample2.__doc__
