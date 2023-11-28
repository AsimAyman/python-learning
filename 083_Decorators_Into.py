#--------------------------------
#-----decorator =>Intro----------
#--------------------------------
# sometimes called meta programming
# everthing in py is object een funcions
# decoratro takes a funciton and add some functionallity and return it
# decorator wrap other funciton and enhance thir behaviour
# decorator is higher order funcion (function accept funtion as parameter)
#--------------------------------
def myDecorator(fun):
    def nested(): #AnyName
        print("before")
        fun()
        print('after')
    return nested

# decorator = myDecorator(sayHello)
# decorator()    


@myDecorator  
def sayHello():
    print("hello");
sayHello()

@myDecorator
def sayHi():
    print("hi")