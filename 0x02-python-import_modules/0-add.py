#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add
    sum = add(a, b)
    print("{0} + {1} = {2}".format(a, b, sum))
