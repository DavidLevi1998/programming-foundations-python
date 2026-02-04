"""
02_control_flow.py

Control flow answers one question:
Which code runs, and when?

Programs are not read top to bottom mechanically.
They branch, repeat, and stop based on conditions.
"""

x = 5

if x > 0:
    print("x is positive")

print("This line always runs")


# --- Conditions are boolean expressions ------------------------------

temperature = 18

if temperature > 25:
    print("hot")
else:
    print("not hot")

# The condition is evaluated once.
# Only one branch runs.


# --- Sequential vs conditional thinking ------------------------------
#
# Many beginners think:
#   "The program checks everything"
#
# Reality:
#   The program follows ONE path.


# --- Loops ------------------------------------------------------------

count = 0

while count < 3:
    print("count is", count)
    count = count + 1

# After the loop ends, execution continues here.
print("done")


# --- Common mistake ---------------------------------------------------
#
# Forgetting to update state inside a loop
# leads to infinite loops.
#
# Always ask:
#   - What changes?
#   - When does this stop?
