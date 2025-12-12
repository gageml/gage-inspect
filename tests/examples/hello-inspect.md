# Hello Inspect example

Run commands from the example dir.

    >>> cd("examples/hello-inspect")

    >>> run("gage task list")
    ╭────────────────┬─────────────────────────────┬───────────╮
    │ Task           │ Description                 │ Source    │
    ├────────────────┼─────────────────────────────┼───────────┤
    │ theory_of_mind │ Inspect AI quick start exa… │ theory.py │
    ╰────────────────┴─────────────────────────────┴───────────╯

Init the command env.

    >>> env = {
    ...     "INSPECT_EVAL_MODEL": "mockllm/model",
    ...     "INSPECT_LOG_DIR": make_temp_dir(),
    ... }

Run the task with fake input and the mock model. We don't expect
anything from this other than a run-through.

    >>> run("gage run theory_of_mind -i Test --target 123 -y", env)
    ┌  Run task
    │
    ◇  Task:
    │  theory_of_mind
    │
    ├  Description:
    │  Inspect AI quick start example.
    │
    ◇  Input:
    │  Test
    │
    ◇  Target:
    │  123
    │
    ◇  Model:
    │  mockllm/model
    │
    ●  Output:
    │
    │  Default output from mockllm/model
    │
    ├  Score:
    │
    │  Incorrect
    │  Grade not found in model output: Default output from
    │  mockllm/model
    │
    └  Done

Run the eval with a limit of 10.

    >>> run("gage eval theory_of_mind -l 10 -y", env)  # +parse
    ┌  Evaluate tasks
    │
    ◇  Tasks:
    │  theory_of_mind
    │
    ◇  Model:
    │  mockllm/model
    │
    ◇  Additional options:
    │  Sample limit: 10
    │
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │theory_of_mind (10 samples): mockllm/model                                    │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    max_tasks: 4, tags: type:eval, dataset: theory_of_mind
    ⤶
    total time:                                   0:00:{}
    ⤶
    model_graded_fact
    accuracy           0.000
    stderr             0.000
    ⤶
    Log:{}.eval
