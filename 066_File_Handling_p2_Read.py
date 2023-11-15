#---------------------------------------
#---Files Handling part 2 => Read file--
#---------------------------------------

myFile = open('myfile.txt','r')
# print(myFile) #<_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'>
# print(myFile.name) #myfile.txt
# print(myFile.mode) #r
# print(myFile.encoding)#cp1252
# print(type(myFile)) #<class '_io.TextIOWrapper'>
# print('-'*40)
# print(myFile.readable)
# print('-'*40)
# print(myFile.read()) # all n of characters and by defualt all -1
# print('-'*40)
# print(myFile.readline()) # the first line
# print('-'*40)
# print(myFile.readlines()) #all the lines in list of string
# print('-'*40)


for line in myFile:
    print(line)

myFile.close()