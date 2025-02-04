#!/usr/bin/python3
'''Module for create a class with list'''


class MyList(list):
    '''A class that inherits from Python's built-in list class'''
    def print_sorted(self):
        '''print a sorted list from this instance'''
        print(sorted(self))
