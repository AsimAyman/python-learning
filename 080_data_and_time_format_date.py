#---------------------------------------
#---------Date and time => format date--
#---------------------------------------
# https://strftime.org/
#--------------------------------------


import datetime 

myBirthDay= datetime.datetime(1993,10,23)
print(myBirthDay.strftime("%a")) #Sat
print(myBirthDay.strftime("%A")) #Saturday
print(myBirthDay.strftime("%b")) #Oct
print(myBirthDay.strftime("%B")) #October
print(myBirthDay.strftime("%d %B %y"))  #23 October 93

