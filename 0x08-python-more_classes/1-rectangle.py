#!/usr/bin/python3

""" this is a class that defines Rectangle class"""
class Rectangle:

    """indicates rectangle class"""

    def __init__(self, width=0, height=0):

        """this method initializes width and height"""

        self.width = width
        self.height = height
    
    @property

    def width(self):

        """a Private instance attribute"""

        return self._width

    @width.setter

    def width(self, value):

        if not isinstance(value, int):
                raise TypeError("width must be an integer")

        if value < 0:

                raise ValueError("width must be >= 0")

        self._width = value

    @property

    def height(self):
         """sets/gets the height of rectangle."""
         return self._height

    @height.setter

    def height(self, value):

        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self._height = value

