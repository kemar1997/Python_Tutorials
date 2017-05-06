# creates a for loop that iterates through nine times starting with 0
# the range function is equivalent to creating a list but within the for loop only
# Remember: Computers always start counting from 0
# the range function also accepts a range of numbers so the iteration doesn't necessarily,
# have to start from exactly 0
# when we have two numbers we have a beginning and an end
"""
when you use three numbers inside of the range function you have the beginning number then
where you want it to end at and lastly the increment value of the range, an example would be
range(10, 40, 5) = this is saying that the range starts at 10 and ends at 40 but goes up by
5 for each number so it would give an output of 10, 15, 20, 25, 30, 35
"""
# for x in range(10, 40, 5):
#     print(x)

"""
A while loop is a special loop that loops as long as the condition is true. So you don't
explicitly give a list or a range of numbers. Keeps looping until a condition becomes false.
"""
x = 2

# keeps outputting the number 5 cause the condition is always true
# creating a way to change the variable so that the while knows when to stop is ideal
# you never really want an infinite loop
while x < 10:
    print(x)
    x += 2
