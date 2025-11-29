from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai._eval.loader import load_tasks

from gage_inspect.dataset import dataset


def test_default_task_dataset():
    tasks = load_tasks(["tests/dataset/test_default_task_dataset.py"], {})
    assert len(tasks) == 1
    task = tasks[0]
    assert task.name == "bar"
    assert task.dataset.name == "bbb"
    assert len(task.dataset) == 1
    assert task.dataset[0] == Sample("bbb")


@task
def bar():
    return Task()


@dataset
def aaa():
    return MemoryDataset([Sample("aaa")])


@dataset(default=True)
def bbb():
    return MemoryDataset([Sample("bbb")])


@dataset
def ccc():
    return MemoryDataset([Sample("ccc")])
