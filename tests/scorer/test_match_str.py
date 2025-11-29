from gage_inspect.scorer._match import match_str


def test_match_exact():
    # Match
    s = match_str("exact", True, "Abc", "Abc")
    assert s.value == "C"
    assert s.answer == "Abc"
    assert s.explanation == "Answer matches target"

    # Match ignore case
    s = match_str("exact", False, "abc", "Abc")
    assert s.value == "C"
    assert s.answer == "Abc"
    assert s.explanation == "Answer matches target (ignore case)"

    # No match
    s = match_str("exact", True, "Abc", "abc")
    assert s.value == "I"
    assert s.answer == "abc"
    assert s.explanation == "Answer does not match target"

    # No match ignore case
    s = match_str("exact", False, "abc", "def")
    assert s.value == "I"
    assert s.answer == "def"
    assert s.explanation == "Answer does not match target (ignore case)"


def test_match_start():
    # Match
    s = match_str("start", True, "Cat", "Cat is green")
    assert s.value == "C"
    assert s.answer == "Cat"
    assert s.explanation == "Answer starts with target"

    # Match ignore case
    s = match_str("start", False, "cat", "Cat is yellow")
    assert s.value == "C"
    assert s.answer == "cat"
    assert s.explanation == "Answer starts with target (ignore case)"

    # No match
    s = match_str("start", True, "cat", "Cat is blue")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Answer does not start with target"

    # No match ignore case
    s = match_str("start", False, "cat", "Dog is blue")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Answer does not start with target (ignore case)"


def test_match_end():
    # Match
    s = match_str("end", True, "blue", "The sky is blue")
    assert s.value == "C"
    assert s.answer == "blue"
    assert s.explanation == "Answer ends with target"

    # Match with trailing period
    s = match_str("end", True, "blue", "The sky is blue.")
    assert s.value == "C"
    assert s.answer == "blue"
    assert s.explanation == "Answer ends with target"

    # Match ignore case
    s = match_str("end", False, "Blue", "The sky is blue")
    assert s.value == "C"
    assert s.answer == "blue"
    assert s.explanation == "Answer ends with target (ignore case)"

    # Match ignore case with trailing period
    s = match_str("end", False, "Blue", "The sky is blue.")
    assert s.value == "C"
    assert s.answer == "blue"
    assert s.explanation == "Answer ends with target (ignore case)"

    # No match
    s = match_str("end", True, "Blue", "The sky is blue")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Answer does not end with target"

    # No match ignore case
    s = match_str("end", False, "red", "The sky is blue")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Answer does not end with target (ignore case)"


def test_match_contains():
    # Match
    s = match_str("contains", True, "tall", "It's tall and here's why.")
    assert s.value == "C"
    assert s.answer == "tall"
    assert s.explanation == "Answer contains target"

    # # Match ignore case
    s = match_str("contains", False, "Tall", "It's tall and here's why.")
    assert s.value == "C"
    assert s.answer == "tall"
    assert s.explanation == "Answer contains target (ignore case)"

    # No match
    s = match_str("contains", True, "Tall", "It's tall and here's why.")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Answer does not contain target"

    # No match ignore case
    s = match_str("contains", False, "big", "It's tall and here's why.")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Answer does not contain target (ignore case)"
