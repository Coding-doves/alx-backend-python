#!/usr/bin/env python3
''' takes str and float/int '''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns tuple(string, float^2) '''
    return k, float(v ** 2)
