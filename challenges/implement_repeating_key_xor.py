#!/usr/bin/env python3
"""
https://cryptopals.com/sets/1/challenges/5
"""
import itertools

lines = """Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"""
expected = (
    '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272'
    'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
)
key = b'ICE'

def vigenere_cipher(text, key):
    """ Repeating key XOR cipher."""
    return bytes(char ^ offset for char, offset in zip(text, itertools.cycle(key)))

if __name__ == '__main__':
    ciphertext = vigenere_cipher(lines.encode(), key).hex()
    assert ciphertext == expected
    print(lines)
