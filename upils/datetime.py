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


def to_timestamp_without_timezone_literal(date: datetime) -> str:
    """Return the time in %Y-%m-%d %H:%M:%S format"""
    return date.strftime("%Y-%m-%d %H:%M:%S")


def from_datetime_literal(datetime_literal: str, datetime_format: str) -> datetime:
    """Parse string datetime to datetime object.
    Datetime without timezone information will be treated as UTC.

    Args:
        datetime_literal: datetime in string format.
        datetime_format: datetime format.

    Returns:
        datetime object.
    """
    parsed_datetime = datetime.strptime(datetime_literal, datetime_format)
    if not parsed_datetime.tzinfo:
        parsed_datetime = parsed_datetime.replace(tzinfo=pytz.UTC)

    return parsed_datetime
