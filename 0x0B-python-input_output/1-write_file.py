#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename (str): string containing name of file
        text (str): text to write to filename

    Returns:
        int: number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        num_char = f.write(text)
    return num_char
