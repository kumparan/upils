"""Module providing all function related to iterable, e.g. List, Tuple, Set"""
from typing import Any, Iterable, List


def replace_none_in_iterable(iterable: Iterable, replacement_value: Any = "") -> List:
    """Replace `None` value in iterable to handle NoneType related exceptions"""
    replaced_none_iterable = []
    if replacement_value is None:
        raise ValueError("Replacement value cannot still be None.")
    for value in iterable:
        if value is None:
            replaced_none_iterable.append(replacement_value)
        else:
            replaced_none_iterable.append(value)
    return replaced_none_iterable
