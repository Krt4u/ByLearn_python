import sys
from loguru import logger

# 记录特定程度的日志
def level_filter(level):
    def is_level(record):
        return record['level'].name == level
    return is_level

logger.remove(0)
logger.add(
    "logs.log",
    filter=level_filter("WARNING"),
    encoding='utf-8'
)
logger.trace("A trace message.")
logger.debug("A debug message.")
logger.info("An info message.")
logger.success("A success message.")
logger.warning("A warning message.")
logger.error("An error message.")
logger.critical("A critical message.")