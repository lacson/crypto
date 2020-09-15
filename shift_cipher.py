#!/usr/bin/env python3
"""
shift_cipher.py
@author lacson
"""
import string
import argparse
from sys import stdin

# define some constants
alphabet = string.ascii_uppercase
alphaset = set(alphabet)

def decrypt(msg: str, key: int) -> str:
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


def encrypt(msg: str, key: int) -> str:
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a string given a key")
    operations = parser.add_mutually_exclusive_group(required=True)
    operations.add_argument("--encrypt", action='store_true', help="Encrypt a message")
    operations.add_argument("--decrypt", action='store_true', help="Decrypt a message")
    operations.add_argument("--brute-decrypt", action='store_true', help="Brute force decrypt a message")
    parser.add_argument('msg', type=str, help="Message to encrypt/decrypt; - to read from STDIN")
    # TODO fix me, key isn't needed if we're brute forcing
    parser.add_argument('key', type=int, help="Key to use for encryption/decryption")
    args = parser.parse_args()

    if args.msg == '-':
        msg = stdin.read()
    else:
        msg = args.msg

    if args.encrypt:
        print("Encrypting '%s' using key %d\nResult: %s" % (msg, args.key, encrypt(msg, args.key)))
    elif args.decrypt:
        print("Decrypting '%s' using key %d\nResult: %s" % (msg, args.key, decrypt(msg, args.key)))
    elif args.brute_decrypt:
        print("Brute force decrypting '%s" % msg)
        for i in range(26):
            print("key=%2d: %s" % (i, decrypt(msg, i)))
    else:
        raise Exception("How did you get here?")