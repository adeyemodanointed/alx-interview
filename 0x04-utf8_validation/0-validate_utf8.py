#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Check for data with bit higher than 11111111 in decimal"""
    for i in data:
        if (i > 255):
            return False
    else:
        return True
