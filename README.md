# Gage Inspect

Gage Inspect extends [Inspect AI][inspect] to support general LLM app
development and running tasks in production endpoints. It's designed for
programmers who want to build LLM applications that leverage Inspect AI
for evaluations.

Inspect AI is open source software used by the AI safety community, AI
labs, and the general community for defining and running evaluations.

Gage Inspect is similarly available as open source software under the
[MIT] license.

Gage Inspect works with [Gage CLI][cli], a set of command line tools
that enable programmer workflows for building and improving Inspect AI
tasks.

Visit [Gage documentation][docs] for a more complete guide to using
Gage.

## Quick start

To use this library, install it using `pip`.

```shell
pip install gage-inspect
```

Here's a simple Inspect task that is run with Gage.

```python
from gage_inspect.task import run_task
from inspect_ai import task, Task
from inspect_ai.solver import prompt_template, generate

@task
def funny():
    return Task(solver=[
        prompt_template(
            "Say something funny about {prompt} in 5 words or less."
        ),
        generate()
    ])

if __name__ == "__main__":
    import sys

    resp = run_task(
        funny(),
        input=sys.argv[1],
        model=sys.argv[2],
    )
    print(resp.completion)
```

To run this task from the command line, save the code to a file named
`funny.py`.

To run this task on OpenAI, you need the `openai` Python package.

```shell
pip install openai
```

Specify the API key required by the provider. For example, define your
API key for OpenAI using `OPENAI_API_KEY`.

```shell
export OPENAI_API_KEY=####
```

Run the task from the command line.

```shell
python funny.py cats openai/gpt-4.1
```

## Task endpoint

Use [FastAPI] to create an endpoint for the task.

```python
from fastapi import FastAPI
from gage_inspect.task import run_task
from funny import funny

app = FastAPI()

@app.get("/funny/{topic}")
def get(topic, model="openai/gpt-4.1"):
    resp = run_task(funny(), topic, model=model)
    return resp.completion
```

Save this code to a file named `serve.py`.

This code requires the `fastapi[standard]` package.

```shell
pip install fastapi[standard]
```

Start an endpoint using the `fastapi` command.

```shell
fastapi serve.py
```

Call the task using curl:

```shell
curl localhost:8000/funny/cats
```

For a more detailed example of serving a task, see
[`examples/add`][add-example].

## Contributing

Please see our [contribution policy][contributing].

<!-- Links -->

[add-example]: ./examples/add/README.md
[cli]: https://github.com/gageml/gage-cli
[contributing]: ./CONTRIBUTING.md
[docs]: https://gage.io/docs
[FastAPI]: https://fastapi.tiangolo.com/
[inspect]: https://inspect.aisi.org.uk/
[MIT]: ./LICENSE
[start]: https://gage.io/start
