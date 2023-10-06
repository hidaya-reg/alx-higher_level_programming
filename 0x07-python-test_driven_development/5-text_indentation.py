#!/usr/bin/python3
"""a function that prints a text with 2 new lines
after each of these characters: ., ?"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: ., ? and :.

    Args:
        text (string): the input text

    Raises:
        TypeError: If 'text' is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    output = ""
    for char in text:
        output += char
        if char in ('.', '?', ':'):
            output += '\n\n'

    lines = output.splitlines()
    for line in lines:
        print(line.strip())
