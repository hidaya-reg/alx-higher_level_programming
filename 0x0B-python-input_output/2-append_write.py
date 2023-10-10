#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): name of file to create or to append into
        text (str): text to append to filename

    Returns:
        int: number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as f:
        num_char = f.write(text)
    return num_char
