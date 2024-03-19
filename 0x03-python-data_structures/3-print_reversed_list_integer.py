#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
  """Prints all integers of a list in reverse order, one per line, using str.format() for integers.

  Args:
    my_list: The list to print in reverse order (default empty list).
  """

  # Iterate through the list in reverse order
  for num in reversed(my_list):
    print("{:d}".format(num))  # Use str.format() to print integer
    print()  # Add a newline after each integer
