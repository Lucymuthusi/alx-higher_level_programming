#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Check for at least one argument
        total = sum(int(arg) for arg in sys.argv[1:])  # Efficient summation using generator expression
        print(total)
    else:
        print("Please provide at least one argument to add.")
