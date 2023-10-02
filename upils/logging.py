"""Module providing custom configuration for loguru"""
import json
import sys

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
    }
    return json.dumps(subset, default=str, ensure_ascii=False) + "\n"


def patching(record):
    """Custom patching for logger serializer"""
    record["extra"]["serialized"] = serialize(record)


def configure_logger(level: str) -> logger:
    """Configuration for custom loguru"""

    # remove default option from loguru. if we don't remove this, it will result in duplicated logs
    logger.remove(0)
    loguru_logger = logger.patch(patching)  # use custom serializer

    loguru_logger.add(
        sink=sys.stdout,
        level=level,
        format="{extra[serialized]}",
    )

    return loguru_logger
