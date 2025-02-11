#!/usr/bin/python3
'''module for file_append'''


def append_write(filename="", text=""):
    '''function appends a string text file and return len of this file'''
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
