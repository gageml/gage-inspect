from inspect_ai.model import (
    ChatMessageAssistant,
    ChatMessageUser,
    Content,
    Model,
    get_model,
)
from inspect_ai.scorer import Score, Target, accuracy, scorer, stderr
from inspect_ai.solver import TaskState


@scorer(metrics=[accuracy(), stderr()])
def llm_judge(model: str | Model | None = None):
    async def score(state: TaskState, target: Target) -> Score:
        nonlocal model

        model = get_model(model)

        # Find user last used user message for prompt
        for msg in reversed(state.messages):
            if isinstance(msg, ChatMessageUser):
                user_prompt = msg.content
                break
        else:
            raise ValueError(
                "cannot score sample - missing ChatMessageUser from messages"
            )

        # Use a dialog to structure the score response
        result = await model.generate(
            llm_judge_dialog(user_prompt, state.output.completion)
        )
        [first, *rest] = result.completion.lstrip().split(" ")
        value = "C" if "yes" in first.lower() else "I"
        explanation = " ".join(rest)
        return Score(value=value, explanation=explanation)

    return score


def llm_judge_dialog(user_prompt: str | list[Content], answer: str):
    return [
        ChatMessageUser(content="I need help scoring the result of a model."),
        ChatMessageAssistant(content="What did you ask the model to do?"),
        ChatMessageUser(
            content=f"Here's the prompt I used: {user_prompt}"
            if isinstance(user_prompt, str)
            else user_prompt
        ),
        ChatMessageAssistant(content="What was the model response?"),
        ChatMessageUser(content=f"The model said this: {answer}"),
        ChatMessageAssistant(
            content=(
                "I'm ready to score the model response. How should I format the score?"
            )
        ),
        ChatMessageUser(
            content=(
                "Say 'Yes' if the model did a good job or 'No' if it didn't. "
                "After Yes or No provide an explanation."
            )
        ),
    ]
