#!/usr/bin/python3
'''module for create a main'''
import sys

'''import the code from the before task'''
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

'''add a name for the file'''
filename = "add_item.json"

'''try to load form a json file add item.json expect FileNotFounderError'''
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)