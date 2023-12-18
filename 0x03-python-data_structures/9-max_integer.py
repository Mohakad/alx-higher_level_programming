#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if ln < 1:
        return None
    else:
        maxx = my_list[0]
        for i in my_list:
            if maxx < i:
                maxx = i
        return maxx
