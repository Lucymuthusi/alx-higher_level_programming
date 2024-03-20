#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
  """
  This function computes the square of all integers in a matrix.

  Args:
      matrix: A 2D list representing the matrix.

  Returns:
      A new 2D list with the squared values of the original matrix.
  """

  # Create a new empty matrix to store the squares
  squared_matrix = []
  
  # Iterate through each row of the original matrix
  for row in matrix:
    # Create a new empty row for the squared matrix
    squared_row = []
    
    # Iterate through each element in the row
    for element in row:
      # Ensure element is an integer before squaring
      if isinstance(element, int):
        squared_element = element * element
      else:
        # Handle non-integer elements (optional: raise an error or use a default value)
        squared_element = None
      squared_row.append(squared_element)
    
    # Add the squared row to the squared matrix
    squared_matrix.append(squared_row)

  return squared_matrix
