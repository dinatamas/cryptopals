#!/usr/bin/env python3
"""
https://cryptopals.com/sets/1/challenges/4
"""
from collections import Counter

from single_byte_xor_cipher import (
    frequency_error,
    frequency_profile,
    solve_single_char_xor
)

if __name__ == '__main__':
    with open('data/4.txt') as f:
        lines = f.read().splitlines()

    best, best_error = None, 1.0
    for line in lines:
        frequencies = frequency_profile(line)
        # Instead of explicitly checking each possible XOR'd string, we just
        # compare the distributions ordered by frequencies. This way we can
        # identify the most matching string even without knowing the offset.
        sorted_frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1]))
        error = frequency_error(sorted_frequencies)
        if error < best_error:
            best, best_error = line, error
    # Then we can solve the single char XOR problem for the best string.
    best, best_offset = solve_single_char_xor(best)
    print(best)
