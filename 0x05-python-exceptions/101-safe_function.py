#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
    except (BaseException) as x:
        result = None
        print("Exception: {}".format(x), file=sys.stderr)
    return result
