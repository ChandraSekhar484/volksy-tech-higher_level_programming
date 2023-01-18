#!/usr/bin/python3
"""It defines a file write_function"""


def write_file(filename="", text=""):
    """writing_file function"""
     lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
