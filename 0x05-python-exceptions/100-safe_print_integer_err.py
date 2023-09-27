#!/usr/bin/python3
"""Safe integer print with error message"""

import sys


def safe_print_integer_err(value):
    """print with error message
    Args:
        value: can be any type (integer, string, etc.)

    Returns:
        boolean: True if value has been correctly printed

    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
    else:
        return True
