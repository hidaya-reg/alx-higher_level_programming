#!/usr/bin/python3
"""inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""
    result_lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        result_lines.append(line)
        if search_string in line:
            result_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(result_lines)
