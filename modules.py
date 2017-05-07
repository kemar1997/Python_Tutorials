"""
Sometimes you are gonna have functions that you want to be used redundantly(over and over),
or maybe not only in the same program but in different programs. So instead of having to
write the function over and over again, what you can do is put all the functions you want
to reuse into its own separate file then include that file in whatever program you are 
working on. First thing you need to do is tell the program you want to include another file,
in order to do that you use the 'import' keyword which basically tells the program or file
to fetch another file to include with the original file. Then you have to tell import what
file you want to use so in this case I wrote "import tuna", and to make a reminder... you 
don't need to add the extension ".py" when importing because it already knows that it is 
another python file unless it won't work, obviously. Second, you have to call the function
from the module you imported. So you have to use dot syntax to say you want to access the 
tuna module and you want to use the fish function in that module
"""

import tuna
import random

tuna.fish()

x = random.randrange(1, 1000)
print(x)