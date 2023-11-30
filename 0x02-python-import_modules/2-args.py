#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv)
    if ln == 2:
        print(f"{ln - 1} argument:")
    elif ln == 1:
        print(f"{ln - 1} arguments.")
    else:
        print(f"{ln - 1} arguments:")
    for i in range(1, ln):
        print(f"{i}: {sys.argv[i]}")
