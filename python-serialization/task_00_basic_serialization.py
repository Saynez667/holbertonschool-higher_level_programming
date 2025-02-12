#!/usr/bin/env python3
'''module for Json'''
import json


def serialize_and_save_to_file(data, filename):
    '''open file in write mode'''
    with open(filename, "w", encoding="utf-8") as file:
        '''serialize the data and save it in the file'''
        return (json.dump(data, file))
    pass

def load_and_deserialize(filename):
    '''open a file in read mode'''
    with open(filename, "r", encoding="utf-8") as file:
        '''load and deserialize a Json content from a file'''
        return (json.load(file))
    pass
