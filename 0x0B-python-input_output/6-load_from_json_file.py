#!/usr/bin/python3
"""Defines a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """a function that creates an Object"""
    with open(filename) as f:
        json.load(f)
