"""Module providing custom configuration for loguru"""
import json
import sys
from typing import Union

from loguru import logger


def serialize(record):
    """Create custom serializer for logging"""
    exception = record["exception"]

    if exception:
        exception = {
            "type": None if exception.type is None else exception.type.__name__,
            "value": exception.value,
            "traceback": bool(exception.traceback),
        }

    subset = {
        "level": record["level"].name,
        "time": {"repr": record["time"], "timestamp": record["time"].timestamp()},
        "message": record["message"],
        "file": {"name": record["file"].name, "path": record["file"].path},
        "line": record["line"],
        "exception": exception,
        "extra": record["extra"]
    }
    return json.dumps(subset, default=str, ensure_ascii=False) + "\n"


def patching(record):
    """Custom patching for logger serializer"""
    record["extra"]["serialized"] = serialize(record)


def configure_logger(level: Union[str, int]) -> logger:
    """
    Configuration for custom loguru

    :param level: logging level. can be str or int.
    https://docs.python.org/3/library/logging.html#logging-levels
    """

    # Remove default option from loguru, if we don't remove this, it will result in duplicated logs.
    # The pre-configured handler is guaranteed to have the index 0.
    # If there is no active handler with such id, it will throw ValueError. If that happens, continue to create logger.
    try:
        logger.remove(0)
    except ValueError:
        pass

    loguru_logger = logger.patch(patching)  # use custom serializer
    loguru_logger.add(
        sink=sys.stdout,
        level=level,
        format="{extra[serialized]}",
    )

    return loguru_logger
