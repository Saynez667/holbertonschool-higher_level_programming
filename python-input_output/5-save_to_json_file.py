#!/usr/bin/python3
'''module for write an Object to a text file'''
import json


def save_to_json_file(my_obj, filename):
    '''function for write an obj to a text file by a json'''
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
