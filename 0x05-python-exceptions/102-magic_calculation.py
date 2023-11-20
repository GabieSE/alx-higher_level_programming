#!/usr/bin/python3


def magic_calculation(x, y):
    rslt = 0
    for idx in range(1, 3):
        try:
            if idx > x:
                raise Exception('Too far')
            else:
                rslt += x ** y / idx
        except:
            rslt = y + x
            break
    return (rslt)
