#-------------------------------------
#-----Modules => Build in modules-----
#-------------------------------------
# module is a file contain a set of functions
# you can import module in your app to help you
# you can import multiple modules
# you can create your own modules
# modules saves your time
#--------------------------------------

#import Main Module
import random
print(random)
print(random.random())

#show all function inside the module
print(dir(random)) 

#improt ine or two function from module
from random import randint, random
from random import *
print(random())
print(randint(100,200))
