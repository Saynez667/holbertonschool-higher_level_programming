#!/usr/bin/python3
'''1-write_file module'''


def write_file(filename="", text=""):
    '''function write a string to a text file and return len of this file'''
    with open(filename, "w", encoding="utf-8") as file:
        return (len(text))
