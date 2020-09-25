#!/usr/bin/env python3

'''
autokey_cipher.py
@author lacson
'''
from utility import alphabet, alphaset

def decrypt(key: int, msg: str) -> str:
    '''
    Decrypts a message given a key.

    :param key: starting key to use
    :param msg: message to decrypt
    :return: the decrypted message
    '''
    ret = ''

    for idx, cha in enumerate(msg.upper()):
        if cha in alphaset:
            if idx == 0:
                ret += alphabet[(alphabet.index(cha) - key) % 26]
            else:
                ret += alphabet[(alphabet.index(cha) - alphabet.index(ret[idx-1])) % 26]
        else:
            ret += cha

    return ret


def encrypt(key: int, msg: str) -> str:
    '''
    Encrypts a message given a key.

    :param key: starting key to use
    :param msg: message to encrypt
    :return: the encrypted message
    '''
    ret = ''

    for idx, cha in enumerate(msg.upper()):
        if cha in alphaset:
            if idx == 0:
                ret += alphabet[(alphabet.index(cha) + key) % 26]
            else:
                ret += alphabet[(alphabet.index(cha) + alphabet.index(msg[idx-1])) % 26]
        else:
            ret += cha

    return ret


def main():
    '''
    Main entrypoint.
    '''
    print("Running self-tests...")
    val = "rendezvous".upper()
    key = 8
    assert val == decrypt(key, encrypt(key, val))

    val = "CPLGHRCJTYKP"
    key = 21
    print("Decrypting {} (key={})".format(val, key))
    print("Result is: {}".format(decrypt(key, val)))


if __name__ == "__main__":
    main()