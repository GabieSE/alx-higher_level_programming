#!/usr/bin/python3
"""Defines Python data structure represented by a JSON string."""

import json

def from_json_string(my_str):
    """a function that returns an object."""
    return json.loads(my_str)
