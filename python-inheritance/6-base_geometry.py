#!/usr/bin/python3
'''Module for create a empty class  BaseGeometry'''


class BaseGeometry:
    '''define a area'''
    def area(self):
        '''raise an exception with the message area is not implemented'''
        raise Exception("area() is not implemented")
