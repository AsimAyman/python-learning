#--------------------------------------------
#-----Exceptinos Handling--------------------
#-----Try | Except | Else | Finally----------
#-------------Advanced Example --------------
#--------------------------------------------

tries = 3
while tries > 0:
    file_name = input("enter the file name")
    
    print(f"you have {tries}")
    tries -=1    