"""Module providing all function related to list"""
from typing import List


def get_unique_list(list_input: List) -> List:
    """Return unique list"""
    return list(set(list_input))
