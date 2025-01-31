#!/usr/bin/python3
'''Module for classes rectangle'''


class Rectangle:
    '''Represents a rectangle'''
    number_of_instances = 0
    symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Retrieve the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Define the area for the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Define perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Return a string of the rectangle using the print_symbol'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.symbol) * self.width
                          for _ in range(self.height)])

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''Print a message when an instance is deleted'''
        '''decrement the class attribute'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
