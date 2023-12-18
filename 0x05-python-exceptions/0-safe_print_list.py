#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    leng = 0
    for ind in range(x):
        try:
            print(my_list[ind], end="")
            leng += 1
        except IndexError:
            break
    print("")
    return leng
