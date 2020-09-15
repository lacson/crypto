#!/usr/bin/env python3

'''
vigenere_cipher.py
@author lacson
'''
import string
import itertools

# define some constants
alphabet = string.ascii_uppercase
alphaset = set(alphabet)

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
