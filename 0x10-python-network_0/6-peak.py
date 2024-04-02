#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak"""
    if not list_of_integers:
        return None
    lenn = len(list_of_integers)
    if lenn == 1:
        return list_of_integers[0]
    elif lenn == 2:
        return max(list_of_integers)

    midl = lenn // 2
    peakk = list_of_integers[midl]
    if peakk > list_of_integers[midl - 1] and peakk > list_of_integers[midl + 1]:
        return peakk
    elif peakk < list_of_integers[midl - 1]:
        return find_peak(list_of_integers[:midl])
    else:
        return find_peak(list_of_integers[midl + 1:])
