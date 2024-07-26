import re


def camel_case_to_snake_case(camel_case_string: str) -> str:
    """
    Convert any one-word string that uses camel case format to snake case.

    :param camel_case_string: A string using camel case format.
    :return: String in snake case format.
    """
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    return pattern.sub("_", camel_case_string).lower()
