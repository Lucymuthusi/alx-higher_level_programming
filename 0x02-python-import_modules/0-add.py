#!/usr/bin/python3

def print_sum(a, b):
  """Prints the sum of a and b in a formatted string."""
  print(f"{a} + {b} = {add(a, b)}")

try:
  from add_0 import add
except ModuleNotFoundError:
  print("Error: Could not import function 'add' from add_0.py")
  exit(1)

a = 1
b = 2

print_sum(a, b)
