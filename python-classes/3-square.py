#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    '''
    Define a simple square and its size
    '''
    def __init__(self, size=0):
        '''
        Initialise a loop to verify if size is an integer
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        '''
        Initialise a loop to verify if size is less than 0
        '''
        if size < 0:
            raise ValueError("size must be >= 0")
        '''
        Initialise size of square
        '''
        self.__size = size

    def area(self):
        '''
        Returns the current area of the square
        '''
        return self.__size
