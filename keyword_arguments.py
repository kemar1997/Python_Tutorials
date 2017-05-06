# name, action, and item are keywords that hold values either strings or numbers
# these keywords can have a default value which can be set in the parentheses below
def dumb_sentence(name='Kemar', action='ate', item='tuna.'):
    print(name, action, item)


dumb_sentence()
# keyword arguments are taken in the function in the order you first put them in as
dumb_sentence('Sally', 'made', 'a banana and strawberry smoothie for breakfast.')

# there are gonna be certain times when you just want to pass in the second argument
# or maybe pass in the third one and so on. whenever you want to pass in a limited
# amount of arguments or pass them in a different order this example shows you how
# First off you need to utilize the keywords of the arguments and equal it to something
# in the parentheses below, so for instance.. i changed the item argument and set it equal
# to "awesome" so when I run it, it returns the sentence "Kemar ate awesome".
dumb_sentence(item='awesome')