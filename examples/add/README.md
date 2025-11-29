# Add task

This example task adds to numbers.

Highlights:

- Use of [`task_doc`] solver, which uses the task docstring to define
  task inputs and outputs. These are used to create a user prompt and
  call [`generate()`].
- [`serve.py`] shows how the task can be served as a [FastAPI] endpoint.
- [`test.py`] defines the task test dataset.

## Prerequisites

- [Install Gage]
- API keys for any models used (e.g. `OPENAI_API_KEY`)
- `curl` to run the command line HTTP request examples below
- The commands below assume you're running from this repository root
  directory

Check the status of your Gage environment.

```shell
gage status
```

## Run the task

```shell
gage run add
```

The task docstring is used to provide hints for the input and target.

The input must be valid YAML or JSON.

To score the task, provide the expected target result.

You can run the task without being prompts by specifying the input along
with `--yes`.

```shell
gage run add --input '{x: 50, y: 51}' --target 101 --yes
```

## Evaluate the task

```shell
gage eval add
```

Gage launches [Inspect AI] to run the evaluation. Inspect AI use the
test cases defined in [`test.py`], which are randomly generated for each
evaluation command.

To evaluate using multiple models at the same time, use `-m, --model`
for each model.

```shell
gage eval add -m openai/gpt-4.1-mini -m openai/gpt-4.1
```

## Review the evaluation results

To review the results of each evaluation run, you can use Gage or
Inspect AI.

Review the evaluations using Gage.

```shell
gage review
```

Review the evaluations using Inspect AI.

```shell
inspect view
```

Visit <http://localhost:7575> to open Inspect View in your browser.

## Serve the task

This example provides [`serve.py`], which shows how a task is run as an
HTTP endpoint.

Use the `fastapi` command to serve the task.

```shell
fastapi run examples/add/serve.py
```

The endpoint supports two different interfaces to the task:

- `POST` to `/add` using a JSON encoded body
- `GET` `/add-alt` using query params

In practice, you will use one interface rather than two. This is an
example to show how different interfaces can be used with FastAPI to
serve tasks.

### `POST /add`

Post to `/add` using `curl`.

```shell
curl http://localhost:8000/add -H 'Content-Type: application/json' -d '{"x": 123, "y": 321}'
```

You can specify additional headers to configure the call.

- Use `x-model` to specify the model used to run the task
- Use `x-target` to specify an expected answer and score the task

Scores are provided using response headers. Use `-v` to see the score
result when you provide a target.

Here's an example of using `gpt-4.1` and including an expected answer
for scoring.

```shell
curl -v http://localhost:8000/add -H 'Content-Type: application/json' -H 'x-model: openai/gpt-4.1' -H 'x-target: 101' -d '{"x": 50, "y": 51}'
```

Note that the HTTP response includes `x-score` and `x-model` headers.

### `GET /add-alt`

Use `curl` to send a request to `/add-alt` using query parameters.

```shell
curl http://localhost:8000/add-alt?x=456&y=654
```

This interface is configured to return JSON content of a two-tuple (JSON
array) containing the answer and an optional score. To score the answer,
include `target` as a query parameter.

```shell
curl http://localhost:8000/add-alt?x=456&y=654&target=1110
```

You can specify a `model` parameter to use a specific model.

```shell
curl http://localhost:8000/add-alt?x=111&y=222&model=openai/gpt-5
```

### FastAPI docs

FastAPI provides OpenAPI/Swagger documentation for the task endpoint.

Visit <http://localhost:8000/docs> to open the task endpoint
documentation in your browser.

Note the two interfaces. You can make requests using either interface by
clicking **Try it out**, which is located within each interface section.
Fill in the dialog input and click **Execute**.

<!-- Links -->

[Install Gage]: https://gage.io/start
[`task_doc`]: ../../src/gage_inspect/solver/_task_doc.py
[`generate()`]:
  https://inspect.aisi.org.uk/reference/inspect_ai.solver.html#generate
[FastAPI]: https://fastapi.tiangolo.com/
[`serve.py`]: ./serve.py
[`test.py`]: ./test.py
[Inspect AI]: https://inspect.aisi.org.uk/
