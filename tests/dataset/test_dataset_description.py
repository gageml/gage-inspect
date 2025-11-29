from inspect_ai._util.registry import (
    registry_lookup,
    registry_info,
)

from gage_inspect.dataset import dataset


@dataset
def sample():
    """A sample dataset."""


def test_dataset_description():
    f = registry_lookup(
        "dataset",  # type: ignore
        "sample",
    )
    assert f is sample
    ds = registry_info(f)
    assert ds.metadata["attribs"] == {"description": "A sample dataset."}
