#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers, one row per line.

  Args:
    matrix: A list of lists representing the matrix (default empty list).
  """

  # Check if the matrix is empty
  if not matrix:
    return

  # Get the number of columns (assuming all rows have the same number of elements)
  num_cols = len(matrix[0])

  # Iterate through each row
  for row in matrix:
    # Check if the row length matches the number of columns
    if len(row) != num_cols:
      print("Error: Row", len(matrix), "has different length than other rows.")
      return  # Exit if row length mismatch is found

    # Print each element in the row, separated by spaces
    for num in row:
      print("{:d}".format(num), end=" ")
    print()
