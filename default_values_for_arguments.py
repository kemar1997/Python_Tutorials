"""
When you have a function that needs extra information in order for it to work, this extra
information are called arguments. They belong in the parentheses when you define a function.
You can also have a default value for functions if you ever need it. The example below will
show how it is done.
"""
"""
When you forget to define a variable explicitly you can be rest assured if you give it
a default value. This can be useful when you have a database but if someone doesn't
answer such question you will get nothing and this could cause an issue in the 
database so it is always helpful to give a variable a default value.
"""


def get_gender(sex="Unknown"):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()
