from gage_inspect.scorer._model import llm_judge_dialog
from inspect_ai.model import ChatMessageAssistant, ChatMessageUser


def test_llm_judge():
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
