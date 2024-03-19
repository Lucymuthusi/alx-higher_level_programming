#!/usr/bin/python3

a = 89
b = 10

# Swap values using XOR and assignment (one-liner)
a, b = b, a ^ b

print("a={:d} - b={:d}".format(a, b))
