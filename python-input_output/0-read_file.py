#!/usr/bin/python3
""""defines read file name"""


def read_file(filename=""):
    """"defining file name with read operation"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
