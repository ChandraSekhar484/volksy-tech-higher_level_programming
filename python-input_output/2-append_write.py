#!/usr/bin/python3
"""it defines an append function"""


def append_write(filename="", text=""):
    """here we are using append function to the file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
