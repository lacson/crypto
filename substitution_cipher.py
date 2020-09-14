#!/usr/bin/env python3
"""
substitution_cipher.py
@author lacson
"""

import string

# declare the key
KEY = {
    'A': 'X',
    'B': 'N',
    'C': 'Y',
    'D': 'A',
    'E': 'H',
    'F': 'P',
    'G': 'O',
    'H': 'G',
    'I': 'Z',
    'J': 'Q',
    'K': 'W',
    'L': 'B',
    'M': 'T',
    'N': 'S',
    'O': 'F',
    'P': 'L',
    'Q': 'R',
    'R': 'C',
    'S': 'V',
    'T': 'M',
    'U': 'U',
    'V': 'E',
    'W': 'K',
    'X': 'J',
    'Y': 'D',
    'Z': 'I'
}

alphaset = set(string.ascii_uppercase)

def encrypt(msg: str) -> str:
    '''
    Encrypts string using the given key.
    
    :param msg: message to encrypt
    :return: encrypted message
    '''
    ret = ''

    for cha in msg.upper():
        if cha not in alphaset:
            ret += cha
        else:
            ret += KEY[cha]

    return ret

def decrypt(msg: str) -> str:
    '''
    Decrypts given cipher text using the given key.
    
    :param msg: cipher text to decrypt
    :return: plain text message
    '''
    ret = ''
    REV_KEY = {v: k for k, v in KEY.items()}

    for cha in msg.upper():
        if cha not in alphaset:
            ret += cha
        else:
            ret += REV_KEY[cha]

    return ret

if __name__ == "__main__":
    # run a brief test
    test_str = "I came I saw I conquered"
    assert encrypt(test_str) == "Z YXTH Z VXK Z YFSRUHCHA"

    to_decrypt = ["KHBYFTH NXYW GFWZHV",
                  "MGZVYZLGHCMHJMYXSSFMNHAHYCDLMHA"]

    for msgs in to_decrypt:
        print("Decrypting %s" % msgs)
        print("Result = %s" % decrypt(msgs))

    