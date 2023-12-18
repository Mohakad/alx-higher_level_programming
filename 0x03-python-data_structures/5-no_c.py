#!/usr/bin/python3
def no_c(my_string):
    newstr = my_string.translate({ord(c): None for c in "cC"})
    return newstr
