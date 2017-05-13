class Parent():

    def print_last_name(self):
        print("Doe")


class Child(Parent):
    def print_first_name(self):
        print("John")

john = Child()
john.print_first_name()
john.print_last_name()
