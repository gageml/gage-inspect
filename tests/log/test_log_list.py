from gage_inspect.log import list_logs


def test_log_list():
    logs = list_logs("tests/log/samples")
    assert len(logs) == 1
    assert logs[0].task == "hello"


def test_deleted_log_list():
    logs = list_logs("tests/log/samples", deleted=True)
    assert len(logs) == 1
    assert logs[0].task == "add"
