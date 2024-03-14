#!/usr/bin/python3
import sys
num_args = len(sys.argv)
print(f"Number of argument{('s' if num_args > 1 else '')}: {num_args}")
print(":" if num_args > 0 else ".")
for i in range(1, num_args):
   print(f"{i+1}: {sys.argv[i]}")
