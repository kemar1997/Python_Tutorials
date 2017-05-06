magicNumber = 26

# the comma in this example allows me to print strings alongside numbers
# print(9, "Kemar")

"""
What the break keyword does is stopping the loop. So in essence the break keyword stops this
loop when the 'magicNumber' is found and stops right there, the break keyword tells the for
loop to loop through 0-100 but when you find the number 26 you can stop.
"""
for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number.")
        break
    else:
        print(n)
