"""Module providing list of function related to date"""
from datetime import datetime

import pytz


def to_rfc3339(date: datetime) -> str:
    """Return the time formatted according to ISO."""
    return date.isoformat(timespec="microseconds") + "Z"


def to_utc7(date: datetime) -> datetime:
    """Return the time in UTC+7"""
    # Datetime without timezone information will be treated as UTC.
    if not date.tzinfo:
        date = date.replace(tzinfo=pytz.UTC)

    utc7_timezone = pytz.timezone("Asia/Jakarta")

    return date.astimezone(tz=utc7_timezone)
