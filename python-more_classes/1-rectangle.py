#!/usr/bin/python3
'''Module for classes rectangle'''


class Rectangle:
    '''Represents a rectangle'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieve the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle'''
        '''if width is not an integer raise TypeError'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        '''if width is less than 0 raise ValueError'''
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieve the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of the rectangle'''
        ''' if height is not an integer raise TypeError'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        '''if value is less than 0 ValueError'''
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
