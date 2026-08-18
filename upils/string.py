"""Module to process and transform strings."""

import hashlib
from base64 import b64encode
from typing import Callable


def hash_and_encode_to_base64(
    data: str, hash_function: Callable = hashlib.sha256
) -> str:
    """Get base64 string from hash digest. Used in surrogate key generation."""
    return b64encode(hash_function(data.encode()).digest()).decode()


def stringify_value(value: str | None, replacement_value: str = "NULL") -> str:
    """Stringify value to use in SQL INSERT statement"""
    if not isinstance(replacement_value, str):
        raise ValueError("Replacement must be a string value.")
    return replacement_value if value is None or value == "" else f"'{value}'"


def format_thousand_separator(val: int | str) -> str:
    """Format numbers in thousands. Only accepts integers or digit-only strings."""
    if isinstance(val, bool) or not isinstance(val, (int, str)):
        raise TypeError(f"Expected int or digit string, got bool: {val!r}")

    if isinstance(val, str):
        val_str = val.strip()
        val_str_to_check = val_str.removeprefix("-")
        if not (val_str_to_check.isdecimal() and val_str_to_check.isascii()):
            raise ValueError(f"Expected digit-only string, got {val!r}")
        val = int(val_str)

    return f"{val:,}".replace(",", ".")
