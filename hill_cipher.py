#!/usr/bin/env python3

'''
hill_cipher.py
@author lacson
'''
DEBUG = False

from utility import *
import math
import numpy

def inv_key(key: numpy.ndarray) -> numpy.ndarray:
    '''
    Given a key, returns the inverse key if possible.
    
    :return: inverted key or None if not possible.
    '''
    # find the determinate of the key
    det = int(numpy.linalg.det(key)) % 26
    invs = mult_inv(26)
    try:
        inv_det = invs[det]
    except KeyError:
        return None

    # multiply the key by the inverted determinate
    # we have to multiply again by the det bc numpy
    # multiplies the array by 1/det
    key_inv = numpy.linalg.inv(key) * numpy.linalg.det(key)
    if DEBUG:
        print("det={}, inv_det={}, key={}".format(det, inv_det, key_inv))
    return inv_det * key_inv % 26


def encrypt(msg: str, key: numpy.ndarray) -> str:
    '''
    Encrypts a message given a key.
    '''
    # make sure it's square
    if key.shape[0] != key.shape[1]:
        raise ArithmeticError("Array must be n x n, receieved {}x{}".format(key.shape[0], key.shape[1]))

    # take the split
    splits = equal_split(key.shape[0], msg.upper())

    # make return string
    ret = ""

    # deal in numbers
    for split in splits:
        converted_nums = [alphabet.index(cha) for cha in split]
        for ind in (numpy.round(numpy.matmul(converted_nums, key)) % 26):
            ret += alphabet[int(ind)]

    return ret


def decrypt(msg: str, key: numpy.ndarray) -> str:
    '''
    Decrypts cipher text given a key.
    '''
    if key.shape[0] != key.shape[1]:
        raise ArithmeticError("Array must be n x n, receieved {}x{}".format(key.shape[0], key.shape[1]))

    # take the inverse of the key
    if inv_key(key) is None:
        return None
    else:
        key_inv = inv_key(key)

    #print(key_inv)

    # take the split
    splits = equal_split(key.shape[0], msg.upper())

    # make return string
    ret = ""

    # deal in numbers
    for split in splits:
        converted_nums = [alphabet.index(cha) for cha in split]
        for ind in (numpy.round(numpy.matmul(converted_nums, key_inv)).astype(int) % 26):
            #print(ind)
            ret += alphabet[ind]

    return ret


def main():
    # run self tests
    key = numpy.array([[5, 4], [1, 9]])
    val = "secure"
    print("Running self tests...")
    assert val.upper() == decrypt(encrypt(val, key), key)

    val = "WZNLQM"
    key = numpy.array([[3, 2], [5, 7]])
    print("Decrypting {}".format(val))
    print("Result = {}".format(decrypt(val, key)))


if __name__ == "__main__":
    main()