def test_patch_scorers():
    from gage_inspect.patch import patch_scorers

    patch_scorers()

    from inspect_ai.scorer import _match

    match_str = _match.__dict__["match_str"]
    assert match_str.__name__ == "patched_match_str"

    # begin
    assert match_str("1", "1", "begin", numeric=True) == ("1", True)
    assert match_str("1 foo", "1", "begin", numeric=True) == ("1 foo", True)
    assert match_str("foo 1", "1", "begin", numeric=True) == ("foo 1", False)

    # end
    assert match_str("1", "1", "end", numeric=True) == ("1", True)
    assert match_str("foo 1", "1", "end", numeric=True) == ("foo 1", True)
    assert match_str("1 foo", "1", "end", numeric=True) == ("1 foo", False)
    assert match_str("1 + 2 = **3**", "3", "end", numeric=True) == (
        "1 + 2 = **3**",
        True,
    )

    # any
    assert match_str("1", "1", "any", numeric=True) == ("1", True)
    assert match_str("foo 1", "1", "any", numeric=True) == ("foo 1", True)
    assert match_str("1 foo", "1", "any", numeric=True) == ("1 foo", True)
    assert match_str("foo 1 bar", "1", "any", numeric=True) == ("foo 1 bar", True)
    assert match_str("foo 2 bar", "1", "any", numeric=True) == ("foo 2 bar", False)

    # exact
    assert match_str("1", "1", "exact", numeric=True) == ("1", True)
    assert match_str("1 foo", "1", "exact", numeric=True) == ("1 foo", False)
    assert match_str("1 2", "1", "exact", numeric=True) == ("1 2", False)
