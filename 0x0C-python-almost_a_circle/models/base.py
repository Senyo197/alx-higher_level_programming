#!/usr/bin/python3
"""Defines a base class"""
import json


class Base:
    """A base class with an initial attribute of 0"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionary into json
        Args:
            list_dictionaries (list of dictionaries): The list of dictionary
            to be converted into json
        Returns:
            str: A JSON string representation of the input list of dictionary
        If list_dictionaries is Null or empty it returns "[]"
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to JSON file
        Arg:
            list_objs (list of Base): A list of instances to be saved
        The filename is based on the class name
        If list_objs id None, an empty will be saved
        The file will be overwritten if it already exist
        """
        if list_objs is None or len(list_objs) == 0:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dict_list)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries
        Args:
            json_string (str): A JSON representation of list of dictionaries
        Returns:
            list: A lsit of dictionaries represented by JSON
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
