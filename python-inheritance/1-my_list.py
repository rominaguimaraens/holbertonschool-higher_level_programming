#!/usr/bin/python3
"""Python Interpreter"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))
