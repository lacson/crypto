#!/usr/bin/env python3

'''
utility.py
helper functions for this crypto schtick
@author lacson
'''
import math


def euler(num: int, debug=False) -> int:
    '''
    Given a number num, calculates
    Euler phi function for num.

    Euler's function is:
    given n, returns how many integers from
    1 - n have a gcd of 1.

    :param num: number to calculate function for
    :return: result of euler phi function
    '''
    ans = [i for i in range(2, num + 1) if math.gcd(i, num) == 1]
    if debug:
        print([1] + ans)
    return len(ans) + 1


def mult_inv(bound: int) -> dict:
    '''
    Given a number bound, finds all the 
    multiplicative inverses
    from {0 .. num}.

    :param bound: range to find, e.g. 26 would be {0 .. 25}
    :return: dictionary of numbers and bounds
    '''
    # make dictionary to return
    ret = {}

    # we know 1 and bound-1 are mult inverses of each other
    ret[1] = 1
    ret[bound-1] = bound-1

    # iterate through the remaining values
    for i in range(2, bound-1):
        if math.gcd(i, bound) == 1 and i not in ret.values():
            # this only works on Py3.8+!
            ans = pow(i, -1, bound)
            ret[i] = ans
            ret[ans] = i

    # return a sorted one
    return {key: value for key, value in sorted(ret.items(), key=lambda item: item[0])}