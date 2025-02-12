#!/usr/bin/env python3
'''module for pickle'''
import pickle


class CustomObject():
    '''Class CustomObject to initialize an instance with name, age, and
    student status'''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

        if not isinstance(name, str):
            raise ValueError("The 'name' parameter must be a string")

        if not isinstance(age, int):
            raise ValueError("The 'age' parameter must be a intergers")

        if not isinstance(is_student, bool):
            raise ValueError("The 'is_student' parameter must be a boolean")

    def Display(self):
        '''Display the object's attributes'''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """Serialize the current instance and save to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename: str):
        """Load an instance from a file and return it."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
