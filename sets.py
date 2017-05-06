"""
A set is a collection of items but, it can not have any duplicates like a list can. And also 
a set is defined with curly braces "{}" instead of square brackets "[]".
"""

groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'}
# prints the list but only prints beer once so it is useless to add duplicates
print(groceries)

# gonna return true since indeed milk is in the groceries set
if 'milk' in groceries:
    print('You already have milk hoss!')
else:
    print("Oh yeah, you need milk!")