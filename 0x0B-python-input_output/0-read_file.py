#!/usr/bin/python3
"""function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout
    Args:
        filename (str): string containing name of file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
