"""
A class variable is anytime you create an object from a class which have variables by
default. And an instance variable is something that is unique to the object. Like for
example this program below has the class Girl and the default gender would be 'female'
and then the name from the __init__ function would be unique and also the instance
variable because every girl would have a different name.
"""


class Girl:

    gender = "female"  # default variable

    def __init__(self, name):
        self.name = name  # instance variable

r = Girl('Rachael')
s = Girl('Susan')
print(r.name + " " + r.gender)
print(s.name + " " + s.gender)
