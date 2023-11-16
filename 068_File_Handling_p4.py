#--------------------------------------
#-----File Handlling =>important info--
#--------------------------------------


myFile = open('file.txt', 'a')
# myFile.truncate(5)
# myFile.write('\r')  #\r \n
# print(myFile.tell()) #71

myFile = open('file.txt', 'r')
myFile.seek(2) #modified the postion of the cuther
print(myFile.read())


import os
os.remove('C:\Users\A\Desktop\python learning\file.txt')