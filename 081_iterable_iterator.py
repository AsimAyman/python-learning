#-----------------------------
#----- Iterable vs iterator---
#-----------------------------
# Iterable
# object constains data that can be iterated upon
# example (String, List, Set, Tuple, Dictionary) 
#-----------------------------
# Iterator 
# object used to iterate over iterable using next() Method return 1 elemtnt at a time
# you can genrate iterator from iterable when useing iter() method
# for loop already call iter() method on the iterable behind the scene
# give stopiteration if theres no next element
#------------------------------

myName = "assem"
for l in myName:
    print(l,end=" ")

print("-"*50)

myIterator = iter(myName)
print(next(myIterator)) #a
print(next(myIterator)) #s
print(next(myIterator)) #s
print(next(myIterator)) #e
print(next(myIterator)) #m
# print(next(myIterator)) # error Tracback stopIteration

for l in iter(myName):
    print(l,end=" ")
