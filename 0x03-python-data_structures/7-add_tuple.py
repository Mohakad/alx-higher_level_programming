#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lna = len(tuple_a)
    lnb = len(tuple_b)
    newtp = ((tuple_a[0] if lna >= 1 else 0) + (tuple_b[0] if lnb >= 1 else 0),
             (tuple_a[1] if lna >= 2 else 0) + (tuple_b[1] if lnb >= 2 else 0))
    return newtp
