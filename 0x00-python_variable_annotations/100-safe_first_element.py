#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""

from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
