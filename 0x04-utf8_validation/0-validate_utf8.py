#!/usr/bin/python3
"""validate_utf8"""


def validUTF8(data):
    """Method checks if data is a valid UTF-8 encoding"""
    for byte in data:
        if byte & 0x80 == 0:
            continue
        elif byte & 0xC0 != 0x80:
            return False
    return True
