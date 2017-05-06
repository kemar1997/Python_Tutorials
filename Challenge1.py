"""
Creating a for loop that loops through zero to one hundred and only prints a multiple of 4
until it reaches to 100.
"""
for x in range(4, 101, 4):
    print(x)
    if 100 < x:
        print("Whoa you have exceeded your normal capacity.")