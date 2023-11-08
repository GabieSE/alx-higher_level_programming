#!/usr/bin/python3


def search_replace(my_list, search, replace):
    return list(map(lambda h: replace if h == search else h, my_list))
