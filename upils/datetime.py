"""Module providing list of function related to date"""
from datetime import datetime


def to_rfc3339(date: datetime) -> str:
    """Return the time formatted according to ISO."""
    return date.isoformat(timespec="microseconds") + "Z"
