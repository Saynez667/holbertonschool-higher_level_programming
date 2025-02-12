#!/usr/bin/python3
'''Module JSON FILE'''
import json


def load_from_json_file(filename):
    '''function for create an object from JSON FILE'''
    with open(filename, "r+", encoding="utf-8") as file:
        return json.load(file)