#!/usr/bin/python3
"""Contains the json string function."""
import json


def from_json_string(my_str):
    """returns the python object represented by a JSON string."""
    return json.loads(my_str)
