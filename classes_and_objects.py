"""
A class is an easy way to group similar variables a.k.a "data" and functions together.
If you want to access anything from a class you must first create an object.
"""


class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('I am dead!')
        else:
            print(str(self.life) + " life left.")

# syntax of an object
enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()