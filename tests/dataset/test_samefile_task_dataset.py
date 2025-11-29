from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai._eval.loader import load_tasks

from gage_inspect.dataset import dataset


def test_samefile_task_dataset():
    tasks = load_tasks(["tests/dataset/test_samefile_task_dataset.py"], {})
    assert len(tasks) == 1
    task = tasks[0]
    assert task.name == "foo"
    assert len(task.dataset) == 2
    assert task.dataset[0] == Sample("Bob")
    assert task.dataset[1] == Sample("Mary")


@task
def foo():
    return Task()


@dataset
def samples():
    return MemoryDataset([Sample("Bob"), Sample("Mary")])
