#!/usr/bin/python3
'''module for inherits from obj a_class'''


def inherits_from(obj, a_class):
    '''Returns True if the object is an instance of a class that directly'''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
