#--------------------------------------------
#-----Decorator => Function with Parameters--
#--------------------------------------------

def myDecorator (func):
    def inner(n1,n2):
        if type(n1) is int and type(n2) is int:
            if n1 >2 or n2 >2:
                print('One of the numbers is greater than 2')
            print("the numbers is int")
            func(n1,n2)

    
    return inner;

def myDecorator2(fun):
    def inner(n1,n2):
        print('from decorator 2')
        fun(n1,n2)
    return inner 
       
@myDecorator
@myDecorator2
def calc(n1, n2): 
    print(n1+n2)

calc(1,3)    



def myDecorator (func):
    def inner(*n):
        for i in n:
            if i <0 :
                print("one of the numbers is less than zero")
        func(*n)
    return inner            


       
@myDecorator
def calc(n1, n2): 
    print(n1+n2)

calc(1,3)    