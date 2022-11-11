#!/usr/bin/env python3
"""
https://cryptopals.com/sets/1/challenges/1
"""
import base64

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
base64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

if __name__ == '__main__':
    # binascii.unhexlify is similar to bytes.fromhex but the latter
    # is more liberal with whitespace. Not sure which to use.
    raw_bytes = bytes.fromhex(hex_string)
    
    # binascii also has base64 decoding/encoding functions but those
    # are not intended to be used directly. Instead, they are used
    # by the functions in the base64 module.
    solution = base64.b64encode(raw_bytes).decode()
    
    assert solution == base64_string
    print(raw_bytes.decode())
