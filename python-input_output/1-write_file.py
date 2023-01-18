#!/usr/bin/python3
"""It defines a file write_function"""


def write_file(filename="", text=""):
    """writing_file function"""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(), end="")
