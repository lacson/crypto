#!/usr/bin/env python3

'''
vigenere_cipher.py
@author lacson
'''
import string
import itertools
from utility import split, encrypt_single, decrypt_single

# define some constants
alphabet = string.ascii_uppercase
alphaset = set(alphabet)


def decrypt(msg: str, key: str) -> str:
    """
    Decrypts given message using key and returns
    plain text.

    :param msg: message to decrypt
    :param key: key to decrypt with
    :return: plain text
    """
    # split the message into a key
    split_msg = split(len(key), msg)

    decrypted_chunks = []
    # iterate through
    for chunk, ind_key in zip(split_msg, key.upper()):
        decrypted_chunks.append(decrypt_single(chunk, alphabet.index(ind_key)))

    # turn chunks back into a string
    zipped_chunks = itertools.zip_longest(*decrypted_chunks)
    zipped_list = list(zipped_chunks)

    # sorry for this line
    # need to filter out Nones in each tuple
    return ''.join([''.join([i for i in j if i is not None]) for j in zipped_list])


def encrypt(msg: str, key: str) -> str:
    """
    Encrypts given message using key and returns
    cipher text.

    :param msg: message to encrypt
    :param key: key to encrypt with
    :return: cipher text
    """
    # split the message into a key
    split_msg = split(len(key), msg)

    decrypted_chunks = []
    # iterate through
    for chunk, ind_key in zip(split_msg, key.upper()):
        decrypted_chunks.append(encrypt_single(chunk, alphabet.index(ind_key)))

    # turn chunks back into a string
    zipped_chunks = itertools.zip_longest(*decrypted_chunks)
    zipped_list = list(zipped_chunks)

    # sorry for this line
    # need to filter out Nones in each tuple
    return ''.join([''.join([i for i in j if i is not None]) for j in zipped_list])


def main():
    CT = "VIEICILMPXMLXYP"
    KEY = "secret"

    # run some tests
    assert encrypt(decrypt(CT, KEY), KEY) == CT
    print("Self-test passed...")

    print("Decrypting {} using key \'{}\'\nResult = {}".format(CT, KEY, decrypt(CT, KEY)))


if __name__ == "__main__":
    main()
