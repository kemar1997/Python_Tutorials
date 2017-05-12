"""
Exceptions are necessary in some cases. Especially when we are dealing with Graphical
User Interfaces.
"""

while True:
    try:
        number = int(input("What is your fav number?\n"))
        result = 18/number
        print(result)
        break
    except ValueError:
        print("Error: Make sure to enter a real number.")
    except ZeroDivisionError:
        print("Choose any other number besides zero. Because logically a number divided by 0 is undefined.")
    finally:
        print("Loop complete")
