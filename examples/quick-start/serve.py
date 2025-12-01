from fastapi import FastAPI
from funny import funny

from gage_inspect.task import run_task

app = FastAPI()


@app.get("/funny/{topic}")
def get_funny(topic, model="openai/gpt-4.1"):
    resp = run_task(funny(), topic, model=model)
    return resp.completion
