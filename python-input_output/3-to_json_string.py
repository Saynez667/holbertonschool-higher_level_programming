#!/usr/bin/python3
import json
'''module for return JSON'''


def to_json_string(my_obj):
    '''return the JSON repr of an object'''
    return json.dumps(my_obj)
