#!/usr/bin/env python3

'''
utility.py
helper functions for this crypto schtick
@author lacson
'''
import math


def euler(num: int) -> int:
    '''
    Given a number num, calculates
    Euler phi function for num.

    Euler's function is:
    given n, returns how many integers from
    1 - n have a gcd of 1.

    :param num: number to calculate function for
    :return: result of euler phi function
    '''
    return len([i for i in range(2, num) if math.gcd(i, num) == 1]) + 1

    