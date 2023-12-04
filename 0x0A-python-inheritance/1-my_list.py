#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""

class MyList(list):
    """a class that inherits from list class."""
    
    def print_sorted(self):
        """a method that prints list class"""
        print(sorted(self))
