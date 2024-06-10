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

    delimiters = ".?:"
    
    # Initialize an empty result string
    result = ""
    
    # Temporary buffer to accumulate characters
    temp = ""
    
    for char in text:
        temp += char
        if char in delimiters:
            result += temp.strip() + "\n\n"
            temp = ""
    
    # Add any remaining text after the last delimiter
    result += temp.strip()
    print(result, end='')
