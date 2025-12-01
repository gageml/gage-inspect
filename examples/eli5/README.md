# Eli5 task example

Task to simplify a statement so a five year old can understand it.

Highlights:

- Paraphrases input in simpler language
- Uses a [separate task](./paws.py) to score results
- Uses benchmark dataset to evaluate the judge

## Prerequisites

- [Install Gage]
- API keys for any models used (e.g. `OPENAI_API_KEY`)

Check the status of your Gage environment.

```shell
gage status
```

## Run the task

```shell
gage run eli5
```

Provide input that you want paraphrased in simpler terms.

## Evaluate the task

```shell
gage eval eli5
```

The task is evaluated using test cases defined in [`samples.yaml`].

Note that tests do not include target information. The judge is an LLM
based task defined in [`paws.py`] and evaluates the task output against
its input.

Specify an alternative model to evaluate the task by specifying the
`judge_model` task argument.

```shell
gage eval eli5 -T judge_model=openai/gpt-5
```

## Evaluate the judge

The task is evaluated using an LLM judge that's implemented as an
Inspect task. The judge can therefore be evaluated using the same method
used to evaluate the task.

The LLM judge tests for paraphrase accuracy. It does not test for
language simplicity. In this respect it's limited. However, given its
limited scope, it can be evaluated using samples from the [PAWS]
benchmark dataset, which tests for paraphrase similarity.

To evaluate the judge, evaluate the `paws` task.

```shell
gage eval paws --limit 100
```

**IMPORTANT** - The PAWS test dataset contains 8,000 entries. Include
`--limit` when evaluating the `paws` task to avoid submitting all 8,000
entries.

You can evaluate multiple LLMs at the same time using `-m / --model`.
This is useful for finding an LLM that performs acceptably at measuring
paraphrase accuracy.

Here's an example of evaluating three models on the `paws` task. Use
`--shuffle` to randomly select the samples to test.

```shell
gage eval paws -l 100 -m openai/gpt-4.1-nano -m openai/gpt-4.1 -m openai/gpt-5 --shuffle
```

<!-- Links -->

[Install Gage]: https://gage.io/start
[`paws.py`]: ./paws.py
[`samples.yaml`]: ./samples.yaml
[PAWS]: https://github.com/google-research-datasets/paws
