#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_in_list = my_list.copy()
    if idx < len(new_in_list):
        new_in_list[idx] = element
    return new_in_list
