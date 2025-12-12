# Hello Inspect

This is a duplicate of the example used in the Inspect AI [walk
through].

This task is typical of an Inspect eval, which measures a specific model
performance characteristic.

> [The task] assesses the ability of a person to infer false beliefs in
> others.

This highlights the difference between _model_ and _application_
evaluation.

A _model_ eval task helps answer the question, "How does this model
perform on this task?"

An _application_ eval helps answer the question, "How does my code,
along with this model, perform on this task?"

Model evals are a mainstay of AI safety researchers.

App evals are central to "eval driven development".

While conceptually these are different concepts, the underlying _task_
abstraction and scoring methods are identical.

## Prerequisites

You're of course free to run the eval using Inspect. To confirm that
Gage can also be used to run the eval (the `gage eval` command is merely
a wrapper around `inspect eval`), ensure that the Gage CLI is installed.

- [Setup Gage for examples][gage-init]
- API keys for models used (e.g. `OPENAI_API_KEY`)

## Run the task

The `theory_of_mind` task is designed to run a full eval. However, you
can use `gage run` to run an hoc example.

```shell
gage run theory_of_mind
```

Here's a sample question you can submit as input:

> Jackson entered the hall. Chloe entered the hall. The boots is in the
> bathtub. Jackson exited the hall. Jackson entered the dining_room.
> Chloe moved the boots to the pantry. Where was the boots at the
> beginning?

The target for this question is:

> bathtub

## Run an eval

Evaluate the task for a model using `gage eval`.

```shell
gage eval theory_of_mind
```

The eval dataset contains 100 samples. To cut down on the eval time (and
cost) use `--limit`.

```shell
gage eval theory_of_mind --limit 20
```

## Review the logs

For a high level review of an eval, use `gage review`.

```shell
gage review
```

Use the arrow keys to navigate to a log file and press `Enter`. To step
through each sample, use the left and right arrow keys.

<!-- Links -->

[walk through]: https://inspect.aisi.org.uk/#sec-hello-inspect
[gage-init]: https://gage.io/examples
