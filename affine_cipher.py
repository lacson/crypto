#!/usr/bin/env python3

'''
affine_cipher.py
@author lacson
'''
import string
import math
from utility import mult_inv

# declare some constants here
ALPHABET = string.ascii_uppercase
ALPHASET = set(ALPHABET)
# wasn't sure how to procedurally generate this?
VALID_A = mult_inv(len(ALPHABET))

def encrypt(msg: str, a: int, b: int) -> str:
    '''
    Encrypts a given message with a given key
    of a and b.

    :param msg: message to encrypt
    :param a: value of a to use
    :param b: value of b to use
    :return: encrypted message
    '''
    if a not in VALID_A.keys():
        print("Error: a={} not valid".format(a))
        return None

    return ''.join([ALPHABET[((a * ALPHABET.index(cha)) + b) % 26] if cha in ALPHASET else cha for cha in msg.upper()])


def decrypt(msg: str, a: int, b: int) -> str:
    '''
    Decrypts a given message with a given key
    of a and b.

    :param msg: cipher text message to decrypt
    :param a: value of a to use
    :param b: value of b to use
    :return: plaintext message
    '''
    if a not in VALID_A.keys():
        print("Error: a={} not valid".format(a))
        return None

    return ''.join([ALPHABET[(VALID_A[a] * (ALPHABET.index(cha) - b)) % 26] if cha in ALPHASET else cha for cha in msg.upper()])


if __name__ == "__main__":
    # run a test on known answer
    a = 9
    b = 5
    KNOWN_PLAIN = "HOKIES"
    KNOWN_ENC = "QBRZPL"
    assert encrypt(KNOWN_PLAIN, a, b) == KNOWN_ENC
    assert decrypt(KNOWN_ENC, a, b) == KNOWN_PLAIN

    print("Self-tests passed, continuing...")

    ENC = "AXG"
    a = 7
    b = 3
    print("Decrypting {} (k = ({},{}))".format(ENC, a, b))
    print("Result is: {}".format(decrypt(ENC, a, b)))