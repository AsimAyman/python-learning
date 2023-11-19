#----------------------------------------
#----Create your module------------------
#----------------------------------------
import sys
paths = sys.path # paths where py research about libs
for p in paths:
    print(p)                

sys.path.append(r'D:\Games')    
for p in paths:  
    print(p)    #it will be added
print('_'*30)

import elzero
print(dir(elzero))

elzero.sayHello('Assem')
elzero.sayHowAreYou("Ayman")
print('_'*30)

# eliasing 
import elzero as ee
ee.sayHello('Ali')
print('_'*30)


from elzero import sayHello
sayHello("Ali")


from elzero import sayHello as sh
sh('mo')



