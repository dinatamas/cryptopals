#!/usr/bin/env python3
"""
https://cryptopals.com/sets/1/challenges/2
"""

# Question: Does Python always parse hex strings as big endian?
lhs = bytes.fromhex('1c0111001f010100061a024b53535009181c')
rhs = bytes.fromhex('686974207468652062756c6c277320657965')
expected = bytes.fromhex('746865206b696420646f6e277420706c6179')

def fixed_xor(lhs, rhs):
    """ XOR two equal-length byte arrays. """
    assert len(lhs) == len(rhs)
    lhs_int = int.from_bytes(lhs, 'big')
    rhs_int = int.from_bytes(rhs, 'big')
    return (lhs_int ^ rhs_int).to_bytes(len(lhs), 'big')

if __name__ == '__main__':
    solution = fixed_xor(lhs, rhs)
    assert solution == expected
    print(solution.decode())
