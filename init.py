"""
Anytime you create an object from a class it looks for an "init" function automatically
when the program is run and whatever is in the init function is call first before any-
thing else. So why would an init function be useful? 
"""


class Tuna:
    def __init__(self):
        print("Brrrlldfljfdg")

    def swim(self):
        print('I am swimming')


# tuna1 = Tuna()
# tuna2 = Tuna()

# tuna1.swim()
# tuna2.__init__()


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(34)
fred = Enemy(52)

fred.get_energy()
jason.get_energy()