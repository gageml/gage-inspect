# `add` example

Run commands from the example dir.

    >>> cd("examples", "add")

    >>> run("gage task list")
    ╭──────┬──────────────────┬────────╮
    │ Task │ Description      │ Source │
    ├──────┼──────────────────┼────────┤
    │ add  │ Add two numbers. │ add.py │
    ╰──────┴──────────────────┴────────╯

Init command env.

    >>> env = {
    ...     "INSPECT_EVAL_MODEL": "mockllm/model",
    ...     "INSPECT_LOG_DIR": make_temp_dir(),
    ... }

Run the `add` task.

    >>> run("gage run add --input '{x: 1, y: 2}' -y", env)
    ┌  Run task
    │
    ◇  Task:
    │  add
    │
    ├  Description:
    │  Add two numbers.
    │
    ◇  Input:
    │  {x: 1, y: 2}
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

Run an eval.

    >>> run("gage eval -y", env)  # +parse
    ┌  Evaluate tasks
    │
    ◇  Tasks:
    │  add
    │
    ◇  Model:
    │  mockllm/model
    │
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │add (100 samples): mockllm/model                                              │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    max_tasks: 4, tags: type:eval, dataset: add_tests
    ⤶
    total time:                                   0:00:{}
    ⤶
    match
    accuracy  0.000
    stderr    0.000
    ⤶
    Log:{}.eval
