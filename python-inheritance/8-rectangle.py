#!/usr/bin/python3
'''Module for creating a Rectangle class that inherits from BaseGeometry'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''Initialize width and height as private attributes and validate'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
