#!/usr/bin/python3
'''Module for classes rectangle'''


class Rectangle:
    '''Represents a rectangle'''
    number_of_instances = 0

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

    def area(self):
        '''define the area for the rectangle'''
        return self.__width * self.__height
    '''return area of rectangle width * height'''
    def perimeter(self):
        '''define perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        '''if width or heigth == 0 return 0'''
        '''return perimeter of rectangle'''
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''Print a message when an instance is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
