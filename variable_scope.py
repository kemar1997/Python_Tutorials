"""
This is just showing the issue of global variables and local variables... so if a variable is
created outside of a function then it can accessed by multiple functions. But if a variable is
declared inside a function then it can only be used inside that function.
"""
a = 7823  # Example of a global variable

def corn():
    # a = 7823 --> Example of a local  variable
    print(a)

def fudge():
    print(a)

corn()
fudge()