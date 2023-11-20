#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    etr = 0

    for t in range(x):
        try:
            
             print("{}".format(my_list[t]), end="")
             etr += 1

        except IndexError:
            break

        print("")

        return (etr)
