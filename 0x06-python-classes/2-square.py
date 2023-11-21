#!/usr/bin/python3

""" defining a class called square"""

class Square:
    
    """ a method that carries two instance, one of them is private """

    def __init__(self, size=0):


        """ Initialize a new square """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        self.__size = size
