"""
Unpacking arguments is very handy in certain instances that can be incorporated in other
programs later on.
"""

def health_calculator(age, apples_eaten, cigs_smoked):
    answer = (100-age) + (apples_eaten * 3.5) - (cigs_smoked * 2)
    print(answer)

kemars_data = [19, 20, 0]

health_calculator(kemars_data[0], kemars_data[1], kemars_data[2])
# this is an example of unpacking arguments from a list
health_calculator(*kemars_data)