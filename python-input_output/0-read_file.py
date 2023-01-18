#!/usr/bin/python3
""""defines read file name"""


def read_file(filename=""):
    """"defining file name with read operation"""
    with open("0-read_file.txt","r")as f:
        f.read_file("0-read_file.txt")
