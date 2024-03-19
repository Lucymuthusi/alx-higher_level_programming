#!/usr/bin/python3

def multiple_returns(sentence):
  """Returns a tuple containing the length of the sentence and its first character (or None for empty strings).

  Args:
    sentence: The input string.

  Returns:
    A tuple with two elements:
      - The length of the sentence (integer).
      - The first character of the sentence (string, or None if empty).
  """

  # Check for empty string
  if not sentence:
    return len(sentence), None

  # Return length and first character
  return len(sentence), sentence[0]
