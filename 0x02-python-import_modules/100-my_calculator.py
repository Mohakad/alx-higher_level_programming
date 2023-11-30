#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    arg = sys.argv[1:]
    leng = len(arg)
    if leng != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    