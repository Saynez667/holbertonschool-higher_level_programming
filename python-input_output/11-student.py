class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of instance with values from a JSON dict"""
        for key, value in json.items():
            setattr(self, key, value)
