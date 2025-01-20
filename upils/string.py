import hashlib
from base64 import b64encode
from typing import Callable


def get_base64_string_from_hash(
    data: str, hash_function: Callable = hashlib.sha256
) -> str:
    """Get base64 string from hash digest. Used in surrogate key generation."""
    return b64encode(hash_function(data.encode()).digest()).decode()
