import os

from inspect_ai import Task, task
from inspect_ai.scorer import Score, Target, accuracy, scorer, stderr
from inspect_ai.solver import TaskState, generate

from gage_inspect.dataset import dataset, structured_input, yaml_dataset
from gage_inspect.solver import input_template
from gage_inspect.task import run_task_async

TEMPLATE = """
Paraphrase the text below so that a five year old can understand it.
Return only the paraphrased text without additional comment.

{input}
"""

DEFAULT_JUDGE = "openai/gpt-4.1"


@task
def eli5(judge: str = DEFAULT_JUDGE) -> Task:
    """Explain something as if I'm five."""

    return Task(
        solver=[
            input_template(TEMPLATE),
            generate(),
        ],
        scorer=paws_task(judge),
    )


@scorer(metrics=[accuracy(), stderr()])
def paws_task(model: str):
    """Score task result using paws task."""

    async def score(state: TaskState, target: Target) -> Score:
        input = structured_input(
            s1=state.input_text,
            s2=state.output.completion,
        )
        resp = await run_task_async(
            f"{resolve_task_dir()}paws.py@paws",
            input,
            model=model,
            tags=["type:score"],
        )
        answer = resp.completion
        if "Yes" in answer:
            value = "C"
            explanation = (
                "Judge said 'Yes' when asked if the response is an accurate paraphrase."
            )
        else:
            value = "I"
            explanation = f"Judge said '{answer}' when asked if the response is an accurate paraphrase."
        return Score(value=value, answer=answer, explanation=explanation)

    return score


@dataset(name="eli5")
def samples():
    """Test samples for eli5 task."""

    return yaml_dataset("samples.yaml")


def resolve_task_dir() -> str:
    cwd = os.getcwd()
    if cwd.endswith("/examples/eli5"):
        return ""
    elif cwd.endswith("/examples"):
        return "eli5/"
    return "examples/eli5/"
