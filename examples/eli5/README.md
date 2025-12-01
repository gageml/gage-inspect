# Eli5 task example

Example task to simplify a statement so a five year old can understand
it.

Highlights:

- Uses a [separate task][paws.py] to score results
- Uses benchmark dataset to evaluate the judge

## Prerequisites

- [Setup Gage for examples][gage-init]
- API keys for models used (e.g. `OPENAI_API_KEY`)

## Run the task

```shell
gage run eli5
```

Provide input that you want simplified.

## Evaluate the task

```shell
gage eval eli5
```

The task is evaluated using test cases defined in
[`samples.yaml`][samples].

Note that tests do not include target information. The judge is an LLM
based task defined in [`paws.py`][paws.py] and evaluates the task output
against its input.

Specify an alternative model to evaluate the task by specifying the
`judge` task argument.

```shell
gage eval eli5 -T judge=openai/gpt-5
```

## Evaluate the judge

The task is evaluated using an LLM judge that's implemented as an
Inspect task. The judge can be evaluated using the same method used to
evaluate the task.

The LLM judge tests for paraphrase accuracy. It does not test for
language simplicity. While in this respect it's limited, it can be
evaluated using samples from the [PAWS][paws-dataset] benchmark dataset,
which tests for paraphrase similarity.

To evaluate the judge, evaluate the `paws` task.

```shell
gage eval paws --limit 100
```

**IMPORTANT** - The PAWS test dataset contains 8,000 entries. Include
`--limit` when evaluating the `paws` task to avoid evaluating all 8,000
entries.

You can evaluate multiple LLMs at the same time using `-m / --model`.
This is useful for finding a model that performs well at measuring
paraphrase accuracy while also minimizing cost.

Here's an example of evaluating three models on the `paws` task. Use
`--shuffle` to randomly select the samples to test.

```shell
gage eval paws -l 100 -m openai/gpt-4.1-nano -m openai/gpt-4.1 -m openai/gpt-5 --shuffle
```

<!-- Links -->

[gage-init]: https://gage.io/examples
[paws.py]: ./paws.py
[samples]: ./samples.yaml
[paws-dataset]: https://github.com/google-research-datasets/paws
