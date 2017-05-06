def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    # using the return keyword to give the girls age
    return girls_age

# then using the function to print out the allowed dating age according to
# what my_age is equal to
kemars_limit = allowed_dating_age(20)
john_doe_limit = allowed_dating_age(32)
print('Kemar can date girls', kemars_limit, 'or older.')
print('John Doe can date girls', john_doe_limit, 'or older.')