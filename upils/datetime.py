"""Module providing list of function related to date"""
from datetime import datetime
from typing import Union

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


def to_timestamp_millis(dt: Union[datetime, str]) -> int:
    """Converting datetime to unix timestamp without changing timezone.

    Args:
        dt: datetime object or str that will be converted.

    Returns:
        Timestamp (millisecond)
    """
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    if isinstance(dt, datetime):
        if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None:
            # remove timezone awareness from timestamptz column value
            dt = dt.replace(tzinfo=None)

    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000
