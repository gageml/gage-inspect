from gage_inspect.dataset._list import list_datasets


def test_dataset_list():
    datasets = list_datasets("tests/dataset/samples")
    assert len(datasets) == 3
    assert datasets[0].model_dump() == {
        "attribs": {},
        "file": "tests/dataset/samples/bar.py",
        "name": "bar",
    }
    assert datasets[1].model_dump() == {
        "attribs": {"description": "Sample dataset"},
        "file": "tests/dataset/samples/foo.py",
        "name": "Foo",
    }
    assert datasets[2].model_dump() == {
        "attribs": {},
        "file": "tests/dataset/samples/foo.py",
        "name": "foo",
    }

    datasets = list_datasets("tests/dataset/samples/bar.py")
    assert len(datasets) == 1
    assert datasets[0].model_dump() == {
        "attribs": {},
        "file": "tests/dataset/samples/bar.py",
        "name": "bar",
    }
