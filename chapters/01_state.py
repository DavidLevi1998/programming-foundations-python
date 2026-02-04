"""
01_state.py

This chapter introduces the idea of *state* in a program.

The goal is not to memorize syntax, but to understand what it means
for a program to have a value now, and a different value later.
"""

# A variable is a *name* bound to a value.
x = 10

# At this point in the program, x refers to the value 10.
print(x)  # 10

# Reassignment does not "change the past".
# It creates a new binding for the same name.
x = 20

print(x)  # 20


# --- State over time -------------------------------------------------

counter = 0
print(counter)  # 0

counter = counter + 1
print(counter)  # 1

counter = counter + 1
print(counter)  # 2

# The important idea:
# The meaning of a name depends on *when* you look at it.


# --- Names vs values -------------------------------------------------

a = 5
b = a

# At this point, both a and b refer to the value 5.
print(a, b)  # 5 5

a = 7

# Reassigning a does NOT affect b.
print(a, b)  # 7 5

# Names are independent.
# Values are not "shared" just because numbers look the same.


# --- Why this matters ------------------------------------------------
#
# Many bugs come from assuming a variable "still means"
# what it meant earlier in the program.
#
# Always ask:
#   - What is the value *right now*?
#   - How did it get here?
#
# State is not mysterious.
# It is simply the history of assignments leading to the current moment.
