#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, other):
        """verify if not equal

        Args:
            other (int): integer to compare current int
        Returns:
            bool: True if not equal, False if esual
        """
        if self is not other:
            return False
        else:
            return True

    def __ne__(self, other):
        """verify equality of two integers

        Args:
            other (int): integer to compare

        Returns:
            bool: True if equal, False otherwise
        """
        if self is not other:
            return True
        return False
