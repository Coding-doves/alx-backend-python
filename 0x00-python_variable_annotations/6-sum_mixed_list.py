#!/usr/bin/env python3
''' sum int and float '''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' return float '''
    return sum(mxd_lst)
