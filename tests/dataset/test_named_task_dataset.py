from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai._eval.loader import load_tasks

from gage_inspect.dataset import dataset


def test_named_task_dataset():
    tasks = load_tasks(["tests/dataset/test_named_task_dataset.py"], {})
    assert len(tasks) == 1
    foo = tasks[0]
    assert foo.name == "baz"
    assert len(foo.dataset) == 1
    assert foo.dataset.name == "baz_samples"
    assert foo.dataset[0] == Sample("Bob")


@task
def baz():
    return Task()


@dataset(task="baz")
def baz_samples():
    return MemoryDataset([Sample("Bob")])


@dataset
def aaa():
    return MemoryDataset([])


@dataset
def zzz():
    return MemoryDataset([])
