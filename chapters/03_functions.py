"""
03_functions.py

Functions are about *abstraction*.

They allow us to give a name to a piece of behavior
and reuse it without rethinking every step.
"""

def square(x):
    return x * x


result = square(4)
print(result)  # 16


# --- Parameters vs arguments -----------------------------------------

def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")

# name is a parameter (inside the function)
# "Alice" is an argument (passed at the call site)


# --- Functions isolate state -----------------------------------------

x = 10

def change_x(x):
    x = 99
    return x

y = change_x(x)

print(x)  # 10
print(y)  # 99

# The x inside the function is NOT the same as the x outside.


# --- Why functions matter --------------------------------------------
#
# Functions let you:
# - control scope
# - reason locally
# - hide irrelevant details
#
# Good functions reduce cognitive load.
