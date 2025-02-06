#!/usr/bin/env python3
'''Module for shapes using abstract base class'''

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''Abstract base class for shapes'''

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape: Shape):
    '''Function to display the area and perimeter of a shape'''
    shape_perimeter = shape.perimeter()
    shape_area = shape.area()
    print(f"Area: {shape_area}")
    print(f"Perimeter: {shape_perimeter}")
