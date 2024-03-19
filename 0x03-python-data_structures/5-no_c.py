def no_c(my_string):
  """Removes all characters 'c' and 'C' (case-insensitive) from a string without using str.replace() or modules.

  Args:
    my_string: The input string.

  Returns:
    A new string with 'c' and 'C' characters removed.
  """

  new_string = ""
  for char in my_string:
    if char.lower() != 'c':  # Check for lowercase 'c'
      new_string += char

  return new_string
