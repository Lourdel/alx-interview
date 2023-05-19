#!/usr/bin/python3

"""validate_utf8"""


def validUTF8(data):
    """Method checks if data is a valid UTF-8 encoding"""
    bit_state = 0
    for num in data:
        bit = 0b10000000
        if not bit_state:
            while (bit & num):
                bit_state += 1
                bit >>= 1
            if bit_state > 4:
                return False
            if bit_state:
                bit_state -= 1
                if bit_state == 0:
                    return False
    return not bit_state
