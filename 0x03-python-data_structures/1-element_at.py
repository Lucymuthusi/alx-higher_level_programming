#!/usr/bin/python3

def element_at(my_list, idx):
  """Retrieves an element from a list at a specified index, similar to C behavior.

  Args:
    my_list: The list to access.
    idx: The index of the element to retrieve.

  Returns:
    The element at the specified index if valid, otherwise None.
  """

  # Check for negative index
  if idx < 0:
    return None

  # Check for index out of range
  if idx >= len(my_list):
    return None

  # Return element at valid index
  return my_list[idx]
