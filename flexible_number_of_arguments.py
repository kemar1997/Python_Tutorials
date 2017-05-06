"""
This is how you build a function that can take any amount of arguments.  What the * does is
in the example below is it is going to be taking a bunch of arguments but it doesn't know 
how many yet. So store them in the "args" variable... however many arguments there are. It 
is common to always name the flexible arguments keyword "args". So the function below takes
any amount of numbers when you call the function and adds them together and gives you an
output. (Just like a calculator)
"""


def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(16, 22)
add_numbers(1433, 2342, 3534, 3238, 6865)