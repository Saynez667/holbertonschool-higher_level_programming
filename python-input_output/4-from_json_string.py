#!/usr/bin/python3
'''module for return an obj repr by a JSON string'''
import json


def from_json_string(my_str):
    '''return an obj by a JSON string'''
    return json.loads(my_str)
