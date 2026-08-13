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
    if isinstance(val, bool):
        raise ValueError(f"Expected int or digit string, got bool: {val}")

    if isinstance(val, str):
        val_str = val.strip()
        if not (val_str.isdecimal() and val_str.isascii()):
            raise ValueError(f"Expected digit-only string, got {val}")
        val = int(val_str)

    if not isinstance(val, int) or val < 0:
        raise ValueError(f"Expected non-negative int or digit string, got {val}")

    return f"{val:,}".replace(",", ".")