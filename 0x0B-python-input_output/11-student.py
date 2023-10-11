#!/usr/bin/python3

"""A class representation of student"""


class Student:
    """Initialization of the new student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the new student class
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json dictionary representation of student
        Returns:
            dictionary representation
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
                return filtered_dict

    def reload_from_json(self, json):
        """Set the attribute for the json data"""
        for key, value in json.items():
            setattr(self, key, value)
