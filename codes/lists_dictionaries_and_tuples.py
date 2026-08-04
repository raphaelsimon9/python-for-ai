# Lists, Dictionaries, and Tuples

"""
Lists are ordered collections of items that can be of different types.
They are mutable, meaning you can change their content after creation.
"""
my_list = ["Alice", 25, "New York", True]

my_list

my_list.append("1.96m")

my_list[0]

my_list[2] = "Atlanta"

my_list[-1] = 1.96

"""
Dictionaries are unordered collections of key-value pairs.
They are mutable, meaning you can change their content after creation.
"""

employee = {
    "name": "Adela",
    "age": 20,
    "city": "New York",
    "is_manager": False,
    "height": 1.70
}

employee

employee["name"] = "Raphael"

employee['name']

employee['has_license'] = True # Appends

del employee['has_license'] # Deletes

print(employee.keys())
print(employee.values())
print(employee.items())


if "Alice" in employee["name"]:
    print("Name Found")
else:
    print("Name Not Found")

name = "Raphael"
if name in employee["name"]:
    print(f"{name} is an employee")
else:
    print(f"{name} is not an employee")


name = "Adela"
if name in employee["name"]:
    employee.update({"age": 31, "city": "Lagos", "job_title": "Data Engineer"})
    print(f"{name} is an employee and her age and city have been updated")
else:
    print(f"{name} is not an employee and her age and city have not been updated")

employee

import math

math.sqrt(16)

from math import sqrt, pow, pi, ceil, floor, factorial, gcd, sin, cos, tan, radians, degrees, log, log10, exp, isclose, isfinite, isinf, isnan, trunc, copysign, fmod, frexp, ldexp, modf, remainder, sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh
sqrt(25)

from math import * # Imports all functions and constants from the math module

print(dir(math))  # Prints all the attributes and methods available in the math module


