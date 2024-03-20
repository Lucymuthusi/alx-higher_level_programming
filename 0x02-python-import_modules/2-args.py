#!/usr/bin/python3

import sys

if __name__ == "__main__":
   num_arguments = len(sys.argv) - 1  # Exclude the script name
   print(f"Number of {'argument' if num_arguments == 1 else 'arguments'}: {num_arguments}.")

   if num_arguments > 0:
       for i in range(1, num_arguments + 1):
           print(f"{i}: {sys.argv[i]}")
