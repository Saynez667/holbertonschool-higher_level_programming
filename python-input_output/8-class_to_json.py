#!/usr/bin/python3
'''module JSON class'''


def class_to_json(obj):
    '''return the dictionnary description with simple data struc '''
    return obj.__dict__
