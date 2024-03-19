#!/usr/bin/python3

def max_integer(my_list=[]):
  """Finds the biggest integer in a list without using the built-in max() function.

  Args:
    my_list: The list of integers (default empty list).

  Returns:
    The biggest integer in the list, or None if the list is empty.
  """

  # Check for empty list
  if not my_list:
    return None

  # Initialize biggest integer with the first element
  biggest = my_list[0]

  # Iterate through the list
  for num in my_list:
    # Update biggest if a larger element is found
    if num > biggest:
      biggest = num

  # Return the biggest integer
  return biggest
