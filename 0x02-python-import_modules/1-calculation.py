#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
