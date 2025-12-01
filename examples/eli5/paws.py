"""
PAWS

Based on: https://github.com/UKGovernmentBEIS/inspect_evals/blob/main/src/inspect_evals/paws/paws.py
"""

from typing import Any

from inspect_ai import Task, task
from inspect_ai.dataset import Sample, hf_dataset
from inspect_ai.solver import generate

from gage_inspect.dataset import dataset, structured_input
from gage_inspect.scorer import match
from gage_inspect.solver import input_template

TEMPLATE = """
Answer Yes if the following two sentences are paraphrases. If they are
not, answer No. Do not give any other answer other than Yes or No in
your response.

Sentence 1: {s1}

Sentence 2: {s2}
"""


@task
def paws() -> Task:
    """Inspect Task implementation of the PAWS benchmark.

    Task compares two sentences and returns 'Yes' if the second sentence
    is a paraphrase of the first or 'No' if it is not.

    Input:
      s1: Sentence 1
      s2: Sentence 2

    Output:
      Yes if s2 is a paraphrase of s1 otherwise No

    """
    return Task(
        solver=[
            input_template(TEMPLATE),
            generate(),
        ],
        scorer=match(),
    )


@dataset(name="paws")
def hf_paws():
    """PAWS dataset from Google Research."""

    return hf_dataset(
        path="google-research-datasets/paws",
        name="labeled_final",  # Required dataset config
        split="test",
        sample_fields=record_to_sample,
    )


def record_to_sample(record: dict[str, Any]) -> Sample:
    return Sample(
        input=structured_input(s1=record["sentence1"], s2=record["sentence2"]),
        target="Yes" if record["label"] == 1 else "No",
        id=record["id"],
    )
