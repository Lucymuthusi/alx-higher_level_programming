#!/usr/bin/python3

def search_replace(my_list, search, replace):
  """
  This function replaces all occurrences of an element with another in a new list.

  Args:
      my_list: The initial list.
      search: The element to replace.
      replace: The new element.

  Returns:
      A new list with all occurrences of 'search' replaced by 'replace'.
  """

  # Create a new empty list to store the replaced elements
  replaced_list = []
  
  # Iterate through each element in the original list
  for element in my_list:
    # Check if the current element is the one to be replaced
    if element == search:
      # Add the replacement element
      replaced_list.append(replace)
    else:
      # Add the original element if it's not the search element
      replaced_list.append(element)

  return replaced_list
