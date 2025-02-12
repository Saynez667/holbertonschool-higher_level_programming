#!/usr/bin/env python3
'''module for pickle'''
import pickle


class CustomObject():
    '''Class CustomObject to initialize an instance with name, age, and stu'''
    def __init__(self, name, age, is_student):
        if not isinstance(name, str):
            raise ValueError("The 'name' parameter must be a string")
        if not isinstance(age, int):
            raise ValueError("The 'age' parameter must be an integer")
        if not isinstance(is_student, bool):
            raise ValueError("The 'is_student' parameter must be a boolean")

        self.name = name
        self.age = age
        self.is_student = is_student

    def Display(self):
        '''Display the object's attributes'''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''Serialize the object and save to a file'''
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        '''Deserialize an object from a file'''
        with open(filename, "rb") as file:
            return pickle.load(file)
