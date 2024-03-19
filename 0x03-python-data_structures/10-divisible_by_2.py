#!/usr/bin/python3

def divisible_by_2(my_list=[]):
  """Finds all multiples of 2 in a list and returns a list of True/False values.

  Args:
    my_list: The list of integers (default empty list).

  Returns:
    A new list with True/False values indicating divisibility by 2 at corresponding positions in the original list.
  """

  # Create an empty list to store divisibility results
  divisibility_list = []

  # Iterate through the original list
  for num in my_list:
    # Check if the element is divisible by 2 using the modulo operator
    divisibility_list.append(num % 2 == 0)

  # Return the list of divisibility results
  return divisibility_list
