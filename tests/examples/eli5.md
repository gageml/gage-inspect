# `eli5` example

Run commands from the example dir.

    >>> cd("examples", "eli5")

    >>> run("gage task list")
    ╭──────┬─────────────────────────────────────────┬─────────╮
    │ Task │ Description                             │ Source  │
    ├──────┼─────────────────────────────────────────┼─────────┤
    │ eli5 │ Explain it like I'm five.               │ eli5.py │
    │ paws │ Inspect implementation of the PAWS ben… │ paws.py │
    ╰──────┴─────────────────────────────────────────┴─────────╯

Init command env.

    >>> env = {
    ...     "INSPECT_EVAL_MODEL": "mockllm/model",
    ...     "INSPECT_LOG_DIR": make_temp_dir(),
    ... }

## `eli5` task

Run task with `--score` to use `paws` task to score.

    >>> run("gage run eli5 -i Test --score -y", env)  # +diff
    ┌  Run task
    │
    ◇  Task:
    │  eli5
    │
    ├  Description:
    │  Explain it like I'm five.
    │
    ◇  Input:
    │  Test
    │
    ◇  Target:
    │  None
    │
    ◇  Model:
    │  mockllm/model
    │
    ◇  Additional options:
    │  Output will be scored
    │
    ●  Output:
    │
    │  Default output from mockllm/model
    │
    ├  Score:
    │
    │  Incorrect
    │  Judge said 'Default output from mockllm/model' when
    │  asked if the response is an accurate paraphrase.
    │
    └  Done

Eval the task. The output shows Additional inspect evals for `paws`
because the LLM judge is a task. This will be cleanup up in a future
release.

    >>> run("gage eval eli5 -y", env)  # +parse
    ┌  Evaluate tasks
    │
    ◇  Tasks:
    │  eli5
    │
    ◇  Model:
    │  mockllm/model
    │
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │eli5 (4 samples): mockllm/model                                               │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    max_tasks: 4, tags: type:eval, dataset: samples
    ⤶
    total time:                                   0:00:{}
    ⤶
    paws_task
    accuracy   0.000
    stderr     0.000
    ⤶
    Log:{}.eval
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:{}
    ⤶
    ⤶
    ⤶
    Log:{}.eval
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:{}
    ⤶
    ⤶
    ⤶
    Log:{}.eval
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:{}
    ⤶
    ⤶
    ⤶
    Log:{}.eval
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:{}
    ⤶
    ⤶
    ⤶
    Log:{}.eval

## `paws` task

The `paws` task is ported from the Inspect PAWS eval. We're using this
as an example of a benchmark dataset being used to test judge
capabilities.

    >>> run("gage run paws --input '{s1: foo, s2: bar}' -y", env)
    ┌  Run task
    │
    ◇  Task:
    │  paws
    │
    ├  Description:
    │  Inspect implementation of the PAWS benchmark.
    │
    ◇  Input:
    │  {s1: foo, s2: bar}
    │
    ◇  Target:
    │  None
    │
    ◇  Model:
    │  mockllm/model
    │
    ●  Output:
    │
    │  Default output from mockllm/model
    │
    └  Done

Run the PAWS eval with a limit of 10. Use a higher timeout to
accommodate database downtime time on new systems.

    >>> run("gage eval paws -l 10 --yes", env, timeout=30)  # +parse
    ┌  Evaluate tasks
    │
    ◇  Tasks:
    │  paws
    │
    ◇  Model:
    │  mockllm/model
    │
    ◇  Additional options:
    │  Sample limit: 10
    │
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (10 samples): mockllm/model                                              │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    max_tasks: 4, tags: type:eval, dataset: google-research-datasets/paws
    ⤶
    total time:                                   0:00:{}
    ⤶
    match
    accuracy  0.000
    stderr    0.000
    ⤶
    Log:{}.eval
