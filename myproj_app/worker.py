import sys
import time

from loguru import logger

logger.remove()
logger.add(sys.stderr, enqueue=True)

def runTask(group_name, group_owner, group_description):
    logger.info("starting runTask")  # in place of actual logging
    time.sleep(5)  # simulate long running task
    logger.info("finished runTask")
    return {group_name: "task complete"}
