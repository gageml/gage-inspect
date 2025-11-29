from gage_inspect.dataset import dataset
from inspect_ai.dataset import MemoryDataset


@dataset
def bar():
    return MemoryDataset([])
