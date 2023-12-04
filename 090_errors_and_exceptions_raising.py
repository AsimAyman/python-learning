#-----------------------------------------
#----Error And Exception Raising----------
#-----------------------------------------
# exception is a runtime error reporting mechanism
# exception gives you the message to understand the proble 
# traceback give you the line t lok for the code in this line
# exceptions have types (SyntaxError, INdexError, KeyError , Etc...)
# exceptions list ''
# laise keyword used to Raise your own Exceptions
#-----------------------------------------

# x = 10 
# if x< 0:
#     print(f"the number {x} is less than zero")
# else:
#     4    

y = "23adsf"
 
if type(y) is not int: # type(y) != int;
    print('only int numbers')

print("continue .....")

if type(y) is not int:
    raise Exception('only int numbers')

print("continue .....")