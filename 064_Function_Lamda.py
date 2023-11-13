#------------------------------
#------Function => lambda------
#------Anonymous Funcion-------
# it has no name
# you can call it inline wihout definding it
# you can use it in return data from anohter function
# lambda used for simple fucciton and def handle the large tasks
# lambda is one single expression not block of code
# lamda type is funcion
#-------------------------------
 
def say_hallo(name): return f"Hello {name}"

hello = lambda name: f"Hello {name}"

print(hello('Ahmed'))

print(say_hallo.__name__) #say_hallo
print(hello.__name__) #<lambda> because it does not have name

print(type(say_hallo)) # <class 'function'>
print(type(hello)) #<class 'function'>