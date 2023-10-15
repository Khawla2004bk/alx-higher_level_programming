#!/usr/bin/python3
"""import json module"""

import json
""" Base calss """


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance.
            Args:
                id (int): id of the new instance
        """
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method def to_json_string(list_dictionaries):
        that returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """
        l_obj = []
        filename = str(cls.__name__) + ".json"
        if list_objs is not None:
            l_o = cls.to_json_string([ob.to_dictionary() for ob in list_objs])
        with open(filename, 'w') as f:
            f.write(l_o)

    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        """
        str_list = []
        if json_string is not None and len(json_string) > 0:
            str_list = json.loads(json_string)
        return (str_list)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all attributes already set
        """
        dummy = cls(0, 0)
        dummy.update(**dictionary)
        return dummy
