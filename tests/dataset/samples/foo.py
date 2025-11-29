from gage_inspect.dataset import dataset
from inspect_ai.dataset import MemoryDataset


@dataset
def foo():
    return MemoryDataset([])


@dataset(name="Foo", description="Sample dataset")
def foo2():
    return MemoryDataset([])
