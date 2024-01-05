#!/usr/bin/python3
def magic_string():
    magic_string.no += 1
    return ("BestSchool, " * (magic_string.no - 1) + "BestSchool")


magic_string.no = 0
