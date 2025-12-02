import json

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from gage_inspect.task import run_task

from examples.add.add import add

DEFAULT_MODEL = "openai/gpt-4.1-mini"


class Input(BaseModel):
    x: int
    y: int


app = FastAPI()
app.state.task = add()


@app.post("/add", response_model=int)
def post_add(req: Request, input: Input):
    """Add x and y.

    Input is submitted as JSON-encoded body.

    Returns the result as a JSON-encoded int.
    """
    resp = run_task(
        req.app.state.task,
        input,
        model=req.headers.get("x-model") or DEFAULT_MODEL,
        target=req.headers.get("x-target"),
        tags=["type:http"],
    )
    return JSONResponse(
        content=int(resp.completion),
        headers={
            "x-model": resp.output.model,
            **(
                {"x-score": str(resp.default_score.value)} if resp.default_score else {}
            ),
        },
    )


@app.get("/add-alt")
def get_add(
    req: Request,
    x: int,
    y: int,
    model: str = DEFAULT_MODEL,
    target: str | None = None,
) -> tuple[int, str | None]:
    """Add x and y.

    Input is provided as query params.

    Returns a JSON encoded list of two items: result and optional score.
    Ouput is scored when `target` is provided, otherwise the value is
    None.
    """
    resp = run_task(
        req.app.state.task,
        json.dumps(dict(x=x, y=y)),
        model=model,
        target=target,
    )
    return (
        int(resp.completion),
        str(resp.default_score.value) if resp.default_score else None,
    )


if __name__ == "__main__":
    print("Run using `fastapi run server.py`")
