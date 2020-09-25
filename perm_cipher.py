#!/usr/bin/env python3

'''
perm_cipher.py
@author lacson
'''
import math, string
from utility import equal_split

# define constants
alphabet = string.ascii_uppercase
alphaset = set(alphabet)


def fix_key(key: dict) -> dict():
    '''
    Given a key, checks to make sure
    it's valid with regards to string indicing.

    :param key: key to check
    :return: fixed key
    '''
    if 0 not in set(key.keys()).union(set(key.values())):
        return {k-1: v-1 for k, v in key.items()}
    else:
        return key


def decrypt(key: dict, msg: str) -> str:
    '''
    Given a key, decrypts a message.

    :param key: key to decrypt with
    :param msg: message to decrypt
    :return: decrypted message
    '''
    # check the key
    key = fix_key(key)

    # first, split the message
    splits = equal_split(len(key.items()), msg.upper())

    # make a str to return to
    ret = ""

    # now, operate on each split:
    for split in splits:
        # flip the dictionary and then sort it again
        for _, v in dict(sorted({v: k for k, v in key.items()}.items())).items():
            ret += split[v]

    # return the string
    return ret


def encrypt(key: dict, msg: str) -> str:
    '''
    Given a key, encrypts a message.

    :param key: key to encrypt with
    :param msg: message to encrypt
    :return: encrypted message
    '''
    # check the key
    key = fix_key(key)
    
    # first, split the message
    splits = equal_split(len(key.items()), msg.upper())

    # make a str to return to
    ret = ""

    # now, operate on each split:
    for split in splits:
        for _, v in key.items():
            ret += split[v]

    # return it
    return ret


def main():
    '''
    Main entrypoint for the scripts.
    '''
    # define the key here
    key = {1:3, 2:5, 3:1, 4:6, 5:4, 6:2}

    # try it out
    print("Running self-tests...")
    val = "letsgohokies"
    assert val.upper() == decrypt(key, encrypt(key, val))

    # run it on provided question
    val = "SLCETATCAKAT"
    print("Decrypting {}".format(val))
    print("Result is {}".format(decrypt(key, val)))


if __name__ == "__main__":
    main()