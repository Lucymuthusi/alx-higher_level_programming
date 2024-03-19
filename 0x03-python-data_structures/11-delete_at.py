#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
  """Deletes the item at a specific position in a list without using pop().

  Args:
    my_list: The list to modify (default empty list).
    idx: The index of the item to delete (default 0).

  Returns:
    A new list with the item at the specified index removed (or the original list if the index is invalid).
  """

  # Check for empty list or negative index
  if not my_list or idx < 0:
    return my_list

  # Check for index out of range
  if idx >= len(my_list):
    return my_list

  # Create a new list (avoiding modification of the original)
  new_list = my_list.copy()

  # Shift elements after the index to the left
  for i in range(idx + 1, len(new_list)):
    new_list[i - 1] = new_list[i]

  # Truncate the new list to remove the last element (which was shifted)
  del new_list[-1]

  # Return the new list with the item deleted
  return new_list
