#!/usr/bin/env python3
''' annotate function '''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' return tuple '''
    return [(i, len(i)) for i in lst]
