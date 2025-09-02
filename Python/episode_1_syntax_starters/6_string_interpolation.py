""" String Interpolation """
# - inserting variables/expressions into strings

# [ f-strings / Formatted String Literals ]
# - declaration          -> f""
# - evaluate expressions -> {}

name = "Buggy"
x, y = 1, 2

print(f"Hi, my name is {name}! {x} + {y} is {x + y}!")