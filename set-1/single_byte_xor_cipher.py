#!/usr/bin/env python3
"""
https://cryptopals.com/sets/1/challenges/3
"""
from collections import Counter

hex_string = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

ENGLISH_LETTER_FREQUENCIES = {
    'a': 0.082, 'g': 0.020,  'l': 0.040, 'q': 0.00095, 'v': 0.0098,
    'b': 0.015, 'h': 0.061,  'm': 0.024, 'r': 0.060,   'w': 0.024,
    'c': 0.028, 'i': 0.070,  'n': 0.067, 's': 0.063,   'x': 0.0015,
    'd': 0.043, 'j': 0.0015, 'o': 0.075, 't': 0.091,   'y': 0.02,
    'e': 0.130, 'k': 0.0077, 'p': 0.019, 'u': 0.028,   'z': 0.00074,
    'f': 0.022,
}

def frequency_profile(text):
    """ Returns the relative character frequencies in the input text. """
    return {char: count / len(text) for char, count in Counter(text.lower()).items()}

def frequency_error(frequencies):
    """
    Returns the total error between the difference of the frequencies in
    the input string and the average frequency values in English texts.
    The frequencies of bigrams and trigrams are not counted.
    Further improvement: frequencies at start / end of words.

    https://en.wikipedia.org/wiki/Frequency_analysis
    https://en.wikipedia.org/wiki/Letter_frequency
    """
    error = 0.0
    for char, count in frequencies.items():
        # Give a default value for non-alpha characters. Some, like spaces,
        # however should be super common, while others (like %) are rare.
        expected = ENGLISH_LETTER_FREQUENCIES.get(char, 0.00001)
        error += abs(count - expected)
    return error

def solve_single_char_xor(text):
    """
    Returns the string that is closest to the English language in terms of
    character frequencies among all single character shifted versions of text.
    """
    best, best_offset, best_error = None, None, 1.0
    # Instead of iterating through each char to shift with, we could also try
    # and find an explicit solution by calculating the difference between the
    # most common chars of both sets (assuming they're both the letter e).
    for offset in range(127):
        original = ''.join(chr(char ^ offset) for char in hex_string)
        if original.isprintable():
            frequencies = frequency_profile(original)
            error = frequency_error(frequencies)
            if error < best_error:
                best, best_offset, best_error = original, offset, error
    return best, best_offset

if __name__ == '__main__':
    best, best_offset = solve_single_char_xor(hex_string)
    print(best)
