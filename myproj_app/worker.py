import asyncio
import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, enqueue=True)

async def run_task(group_name, group_owner, group_description):
    logger.info("starting run_task")
    await asyncio.sleep(5)  # simulate long running task
    logger.info("finished run_task")
    return {group_name: "task complete"}
