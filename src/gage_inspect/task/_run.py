import asyncio

from inspect_ai import Task
from inspect_ai._cli.util import parse_cli_config
from inspect_ai._eval.task.run import TaskRunOptions, task_run
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.log import EvalLog
from inspect_ai.model import ChatMessage, Model
from inspect_ai.util._display import init_display_type
from pydantic import BaseModel

from gage_inspect.task._active import set_active_task

from ._error import NoModel
from ._util import default_log_dir, init_logger, resolve_model, resolve_task


class TaskResponse:
    def __init__(self, log: EvalLog):
        assert log.samples and len(log.samples) == 1, log
        self._sample = log.samples[0]
        self.log = log

    @property
    def sample(self):
        return self._sample

    @property
    def output(self):
        return self._sample.output

    @property
    def completion(self):
        return self._sample.output.completion

    @property
    def score(self):
        return self._sample.score


def run_task(
    task: str | Task,
    input: str | list[ChatMessage] | BaseModel,
    task_args: list[str] | None = None,
    model: str | Model | None = None,
    target: str | None = None,
    log_dir: str | None = None,
    tags: list[str] | None = None,
) -> TaskResponse:
    return asyncio.run(
        run_task_async(task, input, task_args, model, target, log_dir, tags)
    )


async def run_task_async(
    task: str | Task,
    input: str | list[ChatMessage] | BaseModel,
    task_args: list[str] | None = None,
    model: str | Model | None = None,
    target: str | None = None,
    log_dir: str | None = None,
    tags: list[str] | None = None,
) -> TaskResponse:
    # Disable Inspect display
    init_display_type("none")

    # Task
    parsed_task_args = parse_cli_config(task_args or [], None)
    task = resolve_task(task, parsed_task_args)
    set_active_task(task)  # Required for Gage task interface

    # Model
    model = resolve_model(model) or task.model
    if not model:
        raise NoModel()

    # Tags
    tags = tags or []
    tags.append("type:run")

    # Convert model input to JSON
    if isinstance(input, BaseModel):
        input = input.model_dump_json()

    # Input provided via task dataset - must be defined before
    # initializing logger
    task.dataset = MemoryDataset(
        [
            Sample(
                input,
                target=target or "",
                id="run-input",
            )
        ]
    )

    # Logger
    logger = init_logger(
        task,
        parsed_task_args,
        model,
        tags,
        log_dir or default_log_dir(),
    )
    await logger.init()

    # Run task and return log
    log = await task_run(
        TaskRunOptions(
            task,
            model,
            model_roles={},
            sandbox=task.sandbox,
            logger=logger,
            eval_wd="",
            tags=tags,
            score=target is not None,
        )
    )
    return TaskResponse(log)
