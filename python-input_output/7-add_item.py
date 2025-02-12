#!/usr/bin/python3
'''module for create a main'''
import sys

'''import the code from the before task'''
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

'''add a name for the file'''
filename = "add_item.json"

'''Try to load the existing list from the file'''
try:
    items = load_from_json_file(filename)

    '''If the file doesn't exist, start with an empty list'''
except FileNotFoundError:
    items = []
'''add all argument to the list'''
items.extend(sys.argv[1:])

'''save the updated list back to the file'''
save_to_json_file(items, filename)
