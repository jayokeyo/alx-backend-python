#!/usr/bin/env python3
'''
Python - Variable Annotated function sum_list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Computes the sum of floating-point elements within a list.
    '''
    return float(sum(input_list))
