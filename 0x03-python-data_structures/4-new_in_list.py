#!/usr/bin/python3

def new_in_list(my_list, idx, element):
  """Creates a new list by replacing an element at a specific position in the original list, without modifying the original.

  Args:
    my_list: The original list.
    idx: The index of the element to replace.
    element: The new element to insert.

  Returns:
    A new list with the replacement, or a copy of the original list if the index is invalid.
  """

  # Create a copy of the original list
  new_list = my_list.copy()

  # Check for negative index
  if idx < 0:
    return new_list

  # Check for index out of range
  if idx >= len(my_list):
    return new_list

  # Replace element at valid index
  new_list[idx] = element
  return new_list
