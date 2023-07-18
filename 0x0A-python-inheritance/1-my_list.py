#!/usr/bin/python3
"""Defines an inherited list of class MyList."""


class MyList(list):
    """Implements of sorted printing"""

    def print_sorted(self):
        """Print a list in sorted."""
        sorted_ls = sorted(self)
        print(sorted_ls)
