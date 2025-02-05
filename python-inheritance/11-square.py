#!/usr/bin/python3
'''Module for creating a Square class that inherits from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class that inherits from rectangle'''
    def __init__(self, size):
        '''Initialize size as private attribut and validate'''
        self.__size = size
        self.integer_validator("size", size)
        '''super delegue heigth et width a size'''
        super().__init__(size, size)

    def area(self):
        '''return the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''return the area for the square'''
        return f"[Square] {self.__size}/{self.__size}"
