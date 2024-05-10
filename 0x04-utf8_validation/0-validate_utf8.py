#!/usr/bin/python3
"""
module to validate utf-8 encoding
"""


def validUTF8(data):
    """
    This function checks if a list of integers
    represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if the data is a valid UTF-8 encoding, False otherwise.
    """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
