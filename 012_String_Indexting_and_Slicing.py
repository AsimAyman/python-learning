#______________________________________
#----Stirings Indexing and Slicing ----
# All data in python is object
# object contains elements
# every element has its own index
# python use zero-based indexing
# use square brackets to access element
# enable accessing parts of string, tupele or list
#_______________________________________

# Indexing (Access Single Item)
myString = "I love Python"
print(myString[0])  # Index 0 => I
print(myString[9])
print(myString[-1]) # Index -1 => first char from the end
print(myString[-6]) # Index -6 => 6th element from the end p

# Silcing (Access Multiple Squence Item)
#[Start:End:Steps]
# End is not included
print(myString[8:11]) #yth 
print(myString[3:5]) #ov
print(myString[:10]) #if start is not indentefed will start from zero
print(myString[5:]) #if end is not indentefed will go To the end
print(myString[:]) #so will print all string
print(myString[::1]) #Steps is 1 by default
print(myString[::2]) #Ilv yhn
print(myString[-5:-1:]) #ytho
