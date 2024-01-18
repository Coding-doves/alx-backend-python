#!/usr/bin/env python3
''' multipier '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' return function '''
    def multiplier_function(value: float) -> float:
        ''' multiplier '''
        return value * multiplier

    return multiplier_function
