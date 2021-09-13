import sys
from typing import Optional

from fastapi import FastAPI, HTTPException
from loguru import logger
from pydantic import BaseModel
from rq import Queue
from worker import run_task

from redis import Redis

logger.remove()
logger.add(sys.stderr, enqueue=True)


app = FastAPI()
redis_conn = Redis(host="myproj_redis", port=6379, db=0)

q = Queue("my_queue", connection=redis_conn)  # Request body classes


class Group(BaseModel):
    owner: str
    description: Optional[str] = None


@app.get("/hello")
async def hello():
    """Test endpoint"""
    return {"hello": "world"}


@app.post("/groups/{group_name}", status_code=201)
async def add_task(group_name: str, group: Group):
    """
    Adds tasks to worker queue.
    Expects body as dictionary matching the Group class.
    """
    if group_name not in ("group1", "group2"):
        raise HTTPException(status_code=404, detail="Group not found")

    job = q.enqueue(run_task, group_name, group.owner, group.description)

    return {"job": str(job)}
