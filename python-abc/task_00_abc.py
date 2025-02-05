#!/usr/bin/env python3
'''module for import from abc import ABC and abstractmethod'''


from abc import ABC, abstractmethod

'''create a abstract class'''


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


'''Subclasses implementing the abstract method'''


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
