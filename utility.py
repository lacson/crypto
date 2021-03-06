#!/usr/bin/env python3

'''
utility.py
helper functions for this crypto schtick
@author lacson
'''
import math
import string
from collections import deque

alphabet = string.ascii_uppercase
alphaset = set(alphabet)
alphabet_freq = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002, .008, .040, .024, .067, \
    .075, .019, .001, .060, .063, .091, .028, .010, .023, .001, .020, .001]


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
    vals = list(range(2, bound-1))
    for i in vals:
        if math.gcd(i, bound) == 1:
            # this only works on Py3.8+!
            ans = pow(i, -1, bound)
            ret[i] = ans
            # do the inverse too for faster reverse lookup
            ret[ans] = i
            # remove the inverse so we don't iterate on it
            vals.remove(ans)

    # return a sorted one
    return {key: value for key, value in sorted(ret.items(), key=lambda item: item[0])}


def decrypt_single(msg: str, key: int) -> str:
    """
    Decrypts given msg using key and returns
    decrypted message.

    :param msg: message to decrypt
    :param key: key to decrypt with
    :return: decrypted message
    """
    ret = ""
    for cha in msg.upper():
        if cha not in alphaset:
            ret += cha
        else:
            ret += alphabet[(alphabet.index(cha) - key) % len(alphabet)]

    return ret


def encrypt_single(msg: str, key: int) -> str:
    """
    Encrypts given msg using key and returns
    encrypted message.

    :param msg: message to encrypt
    :param key: key to encrypt with
    :return: encrypted message
    """
    ret = ""
    for cha in msg.upper():
        if cha not in alphaset:
            ret += cha
        else:
            ret += alphabet[(alphabet.index(cha) + key) % len(alphabet)]

    return ret


def equal_split(length: int, text: str) -> list():
    '''
    Given a string, creates equal substrings.

    e.g. if we called equal_split(4, "abcdefgh")
    we would get ["abcd", "efgh"]

    :param length: how long to split
    :param text: text to split
    :return: split list of strs
    '''
    return [text[i:i+length] for i in range(0, len(text), length)]


def split(length: int, text: str) -> list():
    '''
    Given a length, bins a string
    into a list of substrings.

    e.g. if we called split(3, "abc")
    we would get ['a', 'b', 'c']

    :param length: how long to split by
    :param text: text to split
    :return: list of strs
    '''
    # make the list to return
    ret = [""] * length

    # iterate through
    for idx, cha in enumerate(text):
        ret[idx % length] += cha

    # return it
    return ret


def count_chars(msg: str, prefill=True) -> dict:
    '''
    Given a string, counts the number of times 
    each alphabetical character occurs in it:

    e.g. "abc" -> {a: 1, b: 1, c: 1}.

    Optionally, we can also prefill so that all
    alphabetical characters appear in the dict:

    e.g. "ab" -> {a: 1, b: 1, c: 0, d: 0, ... z: 0}

    :param msg: string to count
    :param prefill: if true, populate the dict from A-Z first
    :return: dictionary with alphabet counts
    '''
    # strip the string of whitespace and numbers
    # ideally we don't feed garbage but we should safeguard
    stripped_msg = "".join([cha for cha in msg.upper() if cha.isalpha()])

    # make a dictionary:
    if prefill:
        counts = {K: 0 for K in alphabet}
    else:
        counts = {}

    # iterate through the string
    for cha in stripped_msg:
        try:
            counts[cha]
        except KeyError:
            counts[cha] = 1
        else:
            counts[cha] += 1

    return counts


def index_coin(msg: str) -> float:
    '''
    Calculates the index of coincedence for a string.

    :param msg: string to measure
    :return: index of coincendence (float)
    '''
    # get the counts
    counts = count_chars(msg)

    # strip relevant values
    numerator = 0
    vals = [v for v in counts.values() if v >= 2]
    for v in vals:
        numerator += (v * (v-1))
    
    return numerator / (len(msg) * (len(msg) - 1))


def find_dot_prods(msg: str) -> list:
    '''
    Finds the individual vectors and dot products needed to
    figure out the key of a given substring.

    :param msg: message to work on
    :return: list of dot products
    '''
    # get frequency table for substring, throw away the keys
    original_counts = list(count_chars(msg).values())

    # make a list of dot products to return
    ind_dot_prods = []

    # now shift and do the dot product
    for shift in range(26):
        # use deques to make rotating cleaner and faster
        tmp_deque = deque(original_counts)
        tmp_deque.rotate(-shift)
        # find the dot product
        dot_prod = (sum([i * j for i, j in zip(alphabet_freq, tmp_deque)]) / len(msg)) * 100
        ind_dot_prods.append(dot_prod)

    # return the list of dot products
    return ind_dot_prods