"""
Inheritance is basically copying functions from one class to another. Like in this example the Child class inherits
the print_last_name function from the Parent class.  
"""


class Parent():

    def print_last_name(self):
        print("Doe")


class Child(Parent):
    def print_first_name(self):
        print("John")

john = Child()
john.print_first_name()
john.print_last_name()
