# `add` example

Run commands from the example dir.

    >>> cd("examples", "quick-start")

    >>> run("gage task list")
    ╭───────┬───────────────────────────┬──────────╮
    │ Task  │ Description               │ Source   │
    ├───────┼───────────────────────────┼──────────┤
    │ funny │ Gage quick start example. │ funny.py │
    ╰───────┴───────────────────────────┴──────────╯

Init the command env.

    >>> env = {
    ...     "INSPECT_EVAL_MODEL": "mockllm/model",
    ...     "INSPECT_LOG_DIR": make_temp_dir(),
    ... }

Run the task directly as a script.

    >>> run("python funny.py cats mockllm/model", env)
    Default output from mockllm/model

Run the task using `gage`.

    >>> run("gage run funny -i cats -y", env)
    ┌  Run task
    │
    ◇  Task:
    │  funny
    │
    ├  Description:
    │  Gage quick start example.
    │
    ◇  Input:
    │  cats
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

Evaluate the task.

    >>> run("gage eval funny -y", env)  # +parse
    ┌  Evaluate tasks
    │
    ◇  Tasks:
    │  funny
    │
    ◇  Model:
    │  mockllm/model
    │
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │funny (5 samples): mockllm/model                                              │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    max_tasks: 4, tags: type:eval, dataset: samples
    ⤶
    total time:                                   0:00:{}
    ⤶
    llm_judge
    accuracy   0.000
    stderr     0.000
    ⤶
    Log:{}eval
