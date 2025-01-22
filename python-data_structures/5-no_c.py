#!/usr/bin/python3
def no_c(my_string):
    if "c" in my_string or "C" in my_string:
        return my_string.translate({ord('c'): None, ord('C'): None})
    return my_string