#!/usr/bin/env python3
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
    count_ones = 0
    for byte in data:
        # Extract the 8 least significant bits
        byte = byte & 0b11111111

        # Check for invalid byte values (values above 127 or not following
        # UTF-8
        # continuation byte pattern)
        if (byte & 0b10000000) and not (byte & 0b11000000):
            return False

        # Handle multi-byte characters
        if count_ones > 0:
            # Check if continuation byte (starts with 10)
            if not (byte & 0b10000000):
                return False
            count_ones -= 1
        else:
            # Identify the number of bytes for the
            # character based on leading bits
            count_ones = {
                0b00000000: 0,
                0b11000000: 1,
                0b11100000: 2,
                0b11110000: 3,
            }.get(byte >> 7, -1)

            # Invalid starting byte sequence
            if count_ones == -1:
                return False

    # Incomplete character sequence
    return count_ones == 0
