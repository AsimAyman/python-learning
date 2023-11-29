#--------------------------------------------
#-----Decorator => Speed test ---------------
#--------------------------------------------

from time import time

def speedTest(func):
    def wrapper():
        start = time()
        func()
        end  = time()
        print(f'the speed is {end- start}')
    return wrapper


@speedTest
def bigLoop():
    for n in range(1,1000):
        print(n)


bigLoop()