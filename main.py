"""Using python to create multiple decisions of which the computer can decide upon from the given variables
but also have a default decision if the others happen to be false."""

age = 27

if age < 21:
    print("No beer for you!!")
elif age >= 21:
    print("You are allowed to have as much beer as you want. Just drink responsibly!!")

name = 'Kemar'

if name is 'Kemar':
    print("Hey there Kemar.")
elif name is 'Lucy':
    print("Hello Lucy, You don't belong here.")
elif name is 'Thomas':
    print("Hey Thomas, Kemar wanted to say hi to you but you weren't in your office.")
else:
    print(name + ", " + "Please sign up on the following log in page.")