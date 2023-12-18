#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rmap = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }
    pkey = 0
    intt = 0
    for romn in reversed(roman_string):
        key = rmap[romn]
        if key < pkey:
            intt -= key
        else:
            intt += key
        pkey = key
    return intt
