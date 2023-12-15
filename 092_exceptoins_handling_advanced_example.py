#--------------------------------------------
#-----Exceptinos Handling--------------------
#-----Try | Except | Else | Finally----------
#-------------Advanced Example --------------
#--------------------------------------------

the_file = None
tries = 3
while tries > 0:
    try:
        file_name = input("enter the file name => ").strip()
        the_file = file_name.open(the_file,'r')
        print(the_file.read())
        break
    except FileNotFoundError:
        print(f"you have {tries}")
        tries -=1    
    except:
        print(f"you have {tries}")
        print('error is found')
        tries -=1
    finally:
        the_file.close()
        print('final section')    
else:
    print('else section')        