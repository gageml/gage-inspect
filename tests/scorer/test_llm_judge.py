from inspect_ai import Task
from inspect_ai.model import ChatMessageAssistant, ChatMessageUser

from gage_inspect.scorer._model import llm_judge, llm_judge_dialog, parse_judge_answer
from gage_inspect.task import run_task


def test_llm_judge_dialog():
    messages = llm_judge_dialog("Do a thing", "thing")
    assert len(messages) == 7

    assert type(messages[0]) is ChatMessageUser
    assert messages[0].content == "I need help scoring the result of a model."

    assert type(messages[1]) is ChatMessageAssistant
    assert messages[1].content == "What did you ask the model to do?"

    assert type(messages[2]) is ChatMessageUser
    assert messages[2].content == "Here's the prompt I used: Do a thing"

    assert type(messages[3]) is ChatMessageAssistant
    assert messages[3].content == "What was the model response?"

    assert type(messages[4]) is ChatMessageUser
    assert messages[4].content == "The model said this: thing"

    assert type(messages[5]) is ChatMessageAssistant
    assert messages[5].content == (
        "I'm ready to score the model response. How should I format the score?"
    )

    assert type(messages[6]) is ChatMessageUser
    assert messages[6].content == (
        "Say 'Yes' if the model did a good job or 'No' if it didn't. "
        "After Yes or No provide an explanation."
    )


def test_llm_judge_parse_answer():
    assert parse_judge_answer("") == ("I", "")

    # Answer is correct if first part contains 'yes', case insensitive
    assert parse_judge_answer("yes") == ("C", "")
    assert parse_judge_answer("Yes") == ("C", "")
    assert parse_judge_answer("**Yes**") == ("C", "")
    assert parse_judge_answer("Yes-and-no") == ("C", "")

    # Anyting else in first part is incorrect
    assert parse_judge_answer("foo") == ("I", "")
    assert parse_judge_answer("No") == ("I", "")

    # Second part is the exaplanation - separated with any whitespace
    assert parse_judge_answer("Yes. foo bar") == ("C", "foo bar")
    assert parse_judge_answer("Yes.\n\nfoo bar") == ("C", "foo bar")
    assert parse_judge_answer("**Yes** bar foo ") == ("C", "bar foo")
    assert parse_judge_answer("**yes** bar\nfoo") == ("C", "bar\nfoo")


def test_llm_judge_scorer():
    resp = run_task(Task(scorer=llm_judge()), "abc", model="mockllm/model", score=True)
    assert resp.error is None
    assert (
        resp.default_score
        and resp.default_score.explanation == "output from mockllm/model"
    )
