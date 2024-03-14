#!/usr/bin/python3

import sys

# Use a string to handle large numbers accurately
total = 0
for arg in sys.argv[1:]:
   total = str(int(total) + int(arg))

print(total)
