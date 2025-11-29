from inspect_ai._util.registry import (
    registry_lookup,
    registry_info,
)

from inspect_ai.dataset import MemoryDataset

from gage_inspect.dataset import dataset


def lookup(name: str) -> object | None:
    return registry_lookup(
        "dataset",  # type: ignore
        name,
    )


@dataset
def default():
    return MemoryDataset([])


def test_default_dataset_name():
    f = lookup("default")
    assert f is default
    ds = registry_info(f)
    assert ds.name == "default"
    assert ds.metadata == {"attribs": {}, "params": []}


@dataset(name="foo")
def with_name():
    return MemoryDataset([])


def test_dataset_name():
    f = lookup("foo")
    assert f is with_name
    ds = registry_info(f)
    assert ds.name == "foo"
    assert ds.metadata == {"attribs": {}, "params": []}


@dataset(description="Empty test dataset")
def empty():
    return MemoryDataset([])


def test_dataset_attribs():
    f = lookup("empty")
    assert f is empty
    ds = registry_info(f)
    assert ds.name == "empty"
    assert ds.metadata == {
        "attribs": {"description": "Empty test dataset"},
        "params": [],
    }


def test_invalid_dataset_name():
    assert lookup("invalid-name") is None
