#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
  """Adds corresponding elements of two tuples, handling cases of different lengths.

  Args:
    tuple_a: The first tuple (default empty tuple).
    tuple_b: The second tuple (default empty tuple).

  Returns:
    A new tuple containing the sum of corresponding elements from both tuples.
  """

  # Get the lengths of the tuples
  len_a = len(tuple_a)
  len_b = len(tuple_b)

  # Use the maximum length for iteration
  max_len = max(len_a, len_b)

  # Initialize an empty list to store the sum of elements
  result = []
  for i in range(max_len):
    # Use 0 for missing elements
    element_a = tuple_a[i] if i < len_a else 0
    element_b = tuple_b[i] if i < len_b else 0
    # Add corresponding elements
    result.append(element_a + element_b)

  # Return the tuple containing the sum of elements
  return tuple(result)
