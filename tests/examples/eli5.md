# `eli5` example

    >>> cd("examples", "eli5")

    >>> run("gage task list")
    ╭──────┬─────────────────────────────────────────┬─────────╮
    │ Task │ Description                             │ Source  │
    ├──────┼─────────────────────────────────────────┼─────────┤
    │ eli5 │ Explain something as if I'm five.       │ eli5.py │
    │ paws │ Inspect implementation of the PAWS ben… │ paws.py │
    ╰──────┴─────────────────────────────────────────┴─────────╯

## `eli5` task

    >>> run("gage run eli5 --input 'What is a dog?' -m mockllm/model -y")
    ┌  Run task
    │
    ◇  Task:
    │  eli5
    │
    ├  Description:
    │  Explain something as if I'm five.
    │
    ◇  Input:
    │  What is a dog?
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

    >>> run("gage eval eli5 -m mockllm/model -y -T 'judge=mockllm/model'")  # +wildcard
    ┌  Evaluate tasks
    │
    ◇  Tasks:
    │  eli5
    │
    ◇  Model:
    │  mockllm/model
    │
    ◇  Additional options:
    │  Task args: judge=mockllm/model
    │
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │eli5 (4 samples): mockllm/model                                               │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    max_tasks: 4, judge: mockllm/model, tags: type:eval, dataset: samples
    ⤶
    total time:                                   0:00:...
    ⤶
    paws_task
    accuracy   0.000
    stderr     0.000
    ⤶
    Log: ...
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:...
    ⤶
    ⤶
    ⤶
    Log: ...
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:...
    ⤶
    ⤶
    ⤶
    Log: ...
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:...
    ⤶
    ⤶
    ⤶
    Log: ...
    ⤶
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (1 sample): mockllm/model                                                │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    tags: type:score,type:run, dataset: (samples)
    ⤶
    total time:                                   0:00:...
    ⤶
    ⤶
    ⤶
    Log: ...

## `paws` task

    >>> run("gage run paws --input '{s1: \"Hi\", s2: \"Hi there\"}' -m mockllm/model -y")
    ┌  Run task
    │
    ◇  Task:
    │  paws
    │
    ├  Description:
    │  Inspect implementation of the PAWS benchmark.
    │
    ◇  Input:
    │  {s1: "Hi", s2: "Hi there"}
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

    >>> run("gage eval paws -m mockllm/model -y --limit 10", timeout=30)  # +wildcard
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
    │...
    ╭──────────────────────────────────────────────────────────────────────────────╮
    │paws (10 samples): mockllm/model                                              │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    max_tasks: 4, tags: type:eval, dataset: google-research-datasets/paws
    ⤶
    total time:                                   0:00:...
    ⤶
    match
    accuracy  0.000
    stderr    0.000
    ⤶
    Log: ...
