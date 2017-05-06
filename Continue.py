"""
This program prints the numbers 1-20 and continues to search for the numbers in the
numbersTaken list and removes the numbers from being printed leaving us with [1, 3, 4, 6,
7, 8, 9, 10, 11, 14, 15, 16, 18, 19]
"""
numbersTaken = [2, 5, 12, 13, 17]

print("Here are the jersey numbers still available:")

"""
In more detail the continue keyword in a loop tells the loop if anything after the loop is
there just skip it and continue with the initial iteration. Example: So 2 is in the 
numbersTaken list so the continue keyword stops the for loop, so in essence the 2 won't be
printed along with the other numbers and it continues through the iteration until it hits
20. This process also refers to the rest of the numbers in the list.
"""
for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)