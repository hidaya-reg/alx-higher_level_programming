#!/usr/bin/python3
"""create a class MyList"""


class MyList(list):
    """MyList inherit from list"""
    pass

    def print_sorted(self):
        """prints the list but sorted"""
        print(sorted(list(self)))
