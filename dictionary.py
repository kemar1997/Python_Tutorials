"""
A dictionary in python is a set of keys and then those keys are given values as if in RL when
you have a dictionary you have a bunch of words and their definitions.
"""

classmates = {'Bucky':'is cool but smells', 'Emma':'sits behind me', 'Lucy':'asks too many questions'}

# print(classmates)
# print(classmates['Emma'])

for k, v in classmates.items():
    print(k + v)