#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
 """Replaces an element of a list at a specific position, similar to C behavior.

 Args:
   my_list: The list to modify.
   idx: The index of the element to replace.
   element: The new element to insert.

 Returns:
   The original list if the index is invalid, otherwise the modified list.
 """

 # Check for negative index
 if idx < 0:
   return my_list

 # Check for index out of range
 if idx >= len(my_list):
   return my_list

 # Replace element at valid index
 my_list[idx] = element
 return my_list
