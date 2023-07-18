#!/usr/bin/python3

"""Defines the class MyInt, that inherits from int."""


class MyInt(int):
    """change != operator with == behavior."""

    def __ne__(self, other):
        return self.real == other

    """change == opeartor with != behavior."""

    def __eq__(self, other):
        return self.real != other
