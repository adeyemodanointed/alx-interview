#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Check for data with bit higher than 11111111 in decimal"""
    num_bytes = 0
    for i in data:
        if num_bytes == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                num_bytes = 1
            elif i >> 4 == 0b1110:
                num_bytes = 2
            elif i >> 3 == 0b11110:
                num_bytes = 3
            elif i >> 7:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            num_bytes -= 1
        return num_bytes == 0
