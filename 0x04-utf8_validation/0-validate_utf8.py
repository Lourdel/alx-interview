#!/usr/bin/python3
"""validate_utf8"""


def validUTF8(data):
    """Method checks if data is a valid UTF-8 encoding"""
    binary_data = [format(item, f"0{8}b") for item in data]
    for i in binary_data:
        if i[0] == "0" and len(i) == 8:
            return True
        else:
            return False
