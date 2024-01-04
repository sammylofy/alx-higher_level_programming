#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args)
              if num_args > 0 else "0 arguments.")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
