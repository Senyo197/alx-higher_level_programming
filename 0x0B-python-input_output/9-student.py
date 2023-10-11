#!/usr/bin/python3
import json

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

    def to_json(self):
        """json dictionary representation of student
        Returns:
            dictionary representation
        """
        dic_rep = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return json.dumps(dic_rep)
