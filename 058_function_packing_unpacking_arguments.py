#--------------------------------------------------
#---- Function packing, unpacking arguments *Args--
#--------------------------------------------------


print(1,2,3,3,4) #1 2 3 3 4
myList = [1,2,3,4]  
print(myList) #[1, 2, 3, 4]
print(*myList) #1 2 3 4
print('-'*20)

def say_hello(*people):
    for name in people:
        print(f"hello {name}")

say_hello('a','b','c','d')        
print('-'*20)

def show_details(name,*skills):
    print(f'hello {name} your skills is:{skills}')

show_details('assem','php' , 'css' ,'js')    
