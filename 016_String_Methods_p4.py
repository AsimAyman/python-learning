#_____________________________
#-----String Methods----------
#_____________________________

# replace(old, new, count = all)
a = 'Hello one two three one one one two'
print(a.replace('one', '1')) #Hello 1 two three 1 1 1
print(a.replace('two', '2',1)) #Hello one 2 three one one one two

# join(Iterable)
mylist = ["Assem","Ayman","Ibrahim"]
print("_".join(mylist)) #Assem_Ayman_Ibrahim the type is str
