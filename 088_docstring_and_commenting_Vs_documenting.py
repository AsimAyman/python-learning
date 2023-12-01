#--------------------------------------------
#-----Doc String & commenting vs Documenting-
#--------------------------------------------
# documentation string for class, module or function
# can be accessed from the help and doc attributes
# made for understanding the functinoality of teh complex code
# there one line and mutiple line doc strings
#--------------------------------------------

def elzero_function(name):
    '''This function to say Hello''' #it is not a comment
    print(f"Hello {name}")

elzero_function('Ahmed')    
# print(dir(elzero_function))
print(elzero_function.__doc__) #This function to say Hello
help(elzero_function)
# elzero_function(name)
#     This function to say Hello


