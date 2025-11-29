from gage_inspect.log import read_eval_log


def test_read_header():
    log = read_eval_log(
        "tests/log/samples/2025-09-04T12-35-53-05-00_hello_ZeS6vQckR4iDF7wpk4TdZr_001.eval",
        header_only=True,
    )

    assert log.version == 2
    assert log.status == "success"
    assert log.eval.task == "hello"
    assert log.eval.task_id == "ZeS6vQckR4iDF7wpk4TdZr"


def test_read_header_deleted():
    log = read_eval_log(
        "tests/log/samples/2025-09-09T07-16-14-05-00_add_SQLZAGGZEBedtQPD5A8wq6.eval.deleted",
        header_only=True,
    )

    assert log.version == 2
    assert log.status == "success"
    assert log.eval.task == "add"
    assert log.eval.task_id == "SQLZAGGZEBedtQPD5A8wq6"
