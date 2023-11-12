#---------------------------------------
#----Function parameters and arguments--
#---------------------------------------

# def                   => Function keyword define
# say_hello ()          => Fucntion name
# name                  => Parameter
# print(f'Hello {name}')=> Task
# say_hello(a)          => Argument
def say_hello(name):
    print(f'Hello {name}')

a, b,c ='Osama','Ahmed','Sayed'
say_hello(a)
print('-'*50)

def addition(n1, n2):
    if type(n1)!= int or type(n2)!= int:
        print('only integers are allwoed')
    else:
        print (n1 + n2)

addition(100,123)   
addition('as',123)   
print('-'*50)