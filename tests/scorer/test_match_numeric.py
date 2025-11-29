from pytest import raises

from gage_inspect.scorer._match import NumError, match_numeric, output_nums, to_number


def test_output_nums():
    assert output_nums("exact", "123") == [123]
    assert output_nums("start", "321 is the answer") == [321]
    assert output_nums("end", "321 is the answer as is 123") == [123]
    assert output_nums("contains", "321 is the answer as is 123") == [321, 123]
    assert output_nums("contains", "a 1 b 2 c 3 d") == [1, 2, 3]
    assert output_nums("contains", "a b c d") == []

    with raises(NumError) as e:
        assert output_nums("start", "Not sure")

    assert e.value.answer == "Not"


def test_match_numeric_exact():
    # Match
    s = match_numeric("exact", "123", "123")
    assert s.value == "C"
    assert s.answer == "123"
    assert s.explanation == "Answer equals target (numeric)"

    # Non-match
    s = match_numeric("exact", "1.23", "4.56")
    assert s.value == "I"
    assert s.answer == "4.56"
    assert s.explanation == "Answer does not equal target (numeric)"

    # Non-numeric answer
    s = match_numeric("exact", "123", "asd")
    assert s.value == "I"
    assert s.answer == "asd"
    assert s.explanation == "Answer is non-numeric"


def test_match_numeric_start():
    # Match
    s = match_numeric("start", "123", "123 foo")
    assert s.value == "C"
    assert s.answer == "123"
    assert s.explanation == "Answer starts with target (numeric)"

    # Non-match
    s = match_numeric("start", "123", "321 is the answer")
    assert s.value == "I"
    assert s.answer == "321"
    assert s.explanation == "Answer does not start with target (numeric)"

    # Non-numeric answer
    s = match_numeric("start", "123", "foo bar")
    assert s.value == "I"
    assert s.answer == "foo"
    assert s.explanation == "Answer is non-numeric"


def test_match_numeric_end():
    # Match
    s = match_numeric("end", "123", "100 + 23 = 123.")
    assert s.value == "C"
    assert s.answer == "123"
    assert s.explanation == "Answer ends with target (numeric)"

    # Non-match
    s = match_numeric("end", "123", "100 + 23 = 1.123")
    assert s.value == "I"
    assert s.answer == "1.123"
    assert s.explanation == "Answer does not end with target (numeric)"

    # Non-numeric answer
    s = match_numeric("end", "123", "Please rephrase")
    assert s.value == "I"
    assert s.answer == "rephrase"
    assert s.explanation == "Answer is non-numeric"


def test_match_numeric_contains():
    # Match
    s = match_numeric("contains", "321", "The answer is 321, yeah?")
    assert s.value == "C"
    assert s.answer == "321"
    assert s.explanation == "Answer contains target (numeric)"

    # Non match - no candidates
    s = match_numeric("contains", "1.123", "I don't know")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Output does not contain numbers"

    # Non match - one candidate answer
    s = match_numeric("contains", "1.123", "I think it's 4.321")
    assert s.value == "I"
    assert s.answer == "4.321"
    assert s.explanation == "Answer does not contain target (numeric)"

    # Non match - multiple candidates
    s = match_numeric("contains", "1.123", "I think it's 4.321, or maybe 3")
    assert s.value == "I"
    assert s.answer == "Possible answers: 4.321, 3"
    assert s.explanation == "Answer does not contain target (numeric)"


def test_match_numeric_non_numeric_target():
    # Non-numeric target
    s = match_numeric("exact", "asd", "123")
    assert s.value == "I"
    assert s.answer is None
    assert s.explanation == "Target is non-numeric, skipping comparison"


def test_to_number():
    assert to_number("1") == 1
    assert to_number("+1") == 1
    assert to_number("-1") == -1
    assert to_number("1.2") == 1.2
    assert to_number("+1.2") == 1.2
    assert to_number("-1.2") == -1.2
    assert to_number("1e2") == 100.0
    assert to_number("+1e2") == 100.0
    assert to_number("-1e2") == -100.0
    assert to_number("1.01e2") == 101.0
    assert to_number("+1.01e2") == 101.0
    assert to_number("-1.01e2") == -101.0

    # All commas are ignored regardless of correct use/placement
    assert to_number("1,000") == 1000
    assert to_number("1,000,0") == 10_000
    assert to_number("1,000,0.0001") == 10000.0001

    # Trailing '.' is value for a float
    assert to_number("1.") == 1.0

    # Any leading or trailing non-numeric or non-sign chars are ignored
    assert to_number("£1.1") == 1.1
    assert to_number("US$1.2") == 1.2
    assert to_number("2.1$") == 2.1

    with raises(ValueError):
        assert to_number("")

    with raises(ValueError):
        assert to_number("1a2")

    with raises(ValueError):
        assert to_number("1.2.")
