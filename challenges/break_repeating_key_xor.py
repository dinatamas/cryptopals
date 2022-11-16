#!/usr/bin/env python3
"""
https://cryptopals.com/sets/1/challenges/6
"""
import base64

def bitwise_hamming_distance(lhs, rhs):
    """
    Calculates the edit distance between the two strings,
    i.e. the number of different bits between lhs and rhs.
    """
    # The bitwise Hamming distance can be calculated using
    # the XOR operation, which returns True if the two
    # operand bits differ. Count the number of 1s in the result.
    return bin(int.from_bytes(lhs, 'big') ^ int.from_bytes(rhs, 'big')).count('1')
    # In Python 3.10 bit_count() can be used instead of bin(n).count('1')

if __name__ == '__main__':
    with open('data/6.txt') as f:
        # TODO: Is the byteorder always big endian in base64 encoded text?
        raw_bytes = base64.b64decode(f.read())

    assert bitwise_hamming_distance(b'this is a test', b'wokka wokka!!!') == 37

    for keysize in range(2, 41):
        pass
