#!/usr/bin/env python3
'''module for import from abc import ABC and abstractmedthod'''
from abc import ABC, abstractmethod
import math
'''I class the shape with ABC'''
class Shape(ABC):
    '''I use the abstractmethod'''
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
'''for class a Circle with intheration Shape'''
class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius
    def area(self):
        return math.pi*(self.__radius**2)
    def perimeter(self):
        return 2*math.pi*self.__radius
'''for class a Rectangle with intheration Shape'''
class Rectangle(Shape):
    def __init__(self,height,width):
        self.__height = height
        self.__width = width
    def area(self):
        return self.__height * self.__width
    def perimeter(self):
        return 2*(self.__width+self.__height)
def shape_info(shape:Shape):
    shape_perimeter = shape.perimeter()
    shape_area = shape.area()
    print(f"Area: {shape_area}")
    print(f"Perimeter: {shape_perimeter}")