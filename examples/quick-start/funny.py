from inspect_ai import Task, task
from inspect_ai.solver import generate, prompt_template

from gage_inspect.dataset import dataset
from gage_inspect.scorer import llm_judge
from gage_inspect.task import run_task


@task
def funny(judge: str | None = None):
    """Gage quick start example."""
    return Task(
        solver=[
            prompt_template("Say something funny about {prompt} in 5 words or less"),
            generate(),
        ],
        scorer=llm_judge(judge),
    )


@dataset
def samples():
    return ["birds", "cows", "cats", "corn", "barns"]


if __name__ == "__main__":
    import sys

    resp = run_task(
        funny(),
        input=sys.argv[1],
        model=sys.argv[2],
    )
    print(resp.completion)
