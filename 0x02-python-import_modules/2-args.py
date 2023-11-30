#!/usr/bin/python3
import sys
l = len(sys.argv)
if l == 2:
    print(f"{l - 1} argument:")
elif l == 1:
    print(f"{l - 1} arguments.")
else :
    print(f"{l - 1} arguments:")
for i in range(1, l):
    print(f"{i}: {sys.argv[i]}")