#!/usr/bin/python3
'''Module for create a empty class  BaseGeometry'''


class BaseGeometry:
    '''define a area'''
    def area(self):
        '''raise an exception with the message area is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
