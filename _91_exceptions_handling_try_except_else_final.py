#--------------------------------------------
#-----Exceptinos Handling--------------------
#-----Try | Except | Else | Finally----------
#--------------------------------------------
# try => Test the code for errors
# Except => run the code
# Else => if no errors
# finally => run the code
#--------------------------------------------

try:    #try the code
    num = int(input('enter you age: '))
except: #handle if any founded
    print('this is no an ineger')
else:  #if there is no errors
    print('this is a righ input') # instade you can write it in try code
finally: 
    print("i will execute the code what ever happened")


try:
    print(10/0)  #zero divide error 
    print(x)  
except ZeroDivisionError:
    print(-99)
except NameError:
    print('not found') 
except:
    print("error happed")       