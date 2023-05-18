#!/usr/bin/python3
"""validate_utf8"""


def validUTF8(data):
    """Method checks if data is a valid UTF-8 encoding"""
    binary_data = [format(item, f"0{8}b") for item in data]
    for i in binary_data:
        if i.startswith("0"):
            continue
        elif i.startswith("110"):
            num_bytes = 2
        elif i.startswith("1110"):
            num_bytes = 3
        elif i.startswith("11110"):
            num_bytes = 4
        else:
            return False

    return True
