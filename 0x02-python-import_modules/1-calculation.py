#!/usr/bin/python3

# Import all functions from calculator_1.py
from calculator_1 import *  # Assuming all functions are defined here

# Define variables a and b
a = 10
b = 5

# Call and print addition result
print(f"{a} + {b} = {add(a, b)}")

# Call and print subtraction result
print(f"{a} - {b} = {subtract(a, b)}")

# Call and print multiplication result
print(f"{a} * {b} = {multiply(a, b)}")

# Call and print division result
print(f"{a} / {b} = {divide(a, b)}")
