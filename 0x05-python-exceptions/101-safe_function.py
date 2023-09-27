#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely and handles exceptions

    Args:
        fct (callable): function to execute
        *args: argument lit to pass to fct

    Returns:
        Any: the result of the fct

    """

    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
    else:
        return result
