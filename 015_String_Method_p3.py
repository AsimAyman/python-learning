#_____________________________
#-----String Methods----------
#_____________________________

#index(SubSting, start, end)
a = "I love python"
print(a.index("l")); #2
print(a[a.index("l")]) #l
print(a.index("o")); #3
#print(a.index("k")); #error

#find(SubSting, start, end) returns -1 if not found
print(a.find("k",)); #-1

#rjust() ljust()
c = "Osama"
print(c.rjust(21,'-')) #--------------------Osama and space by the defult
print(c.ljust(23,'*')) #Osama******************

#splitlines()
e ="""First line
 Second line
 Third line"""
print(e.splitlines()) #['First line', ' Second line', ' Third line']
print(type(e.splitlines())) #<class 'list'>
f = "first line \nSecond line \nThird line"
print(f.splitlines()) #['first line ', 'Second line ', 'Third line']

#expandTabs()
g =    "Hello\t world!\tFirst"
print(g.expandtabs(20)) #

one = "I love python and 3G"
print(one.istitle()) #False

two = "  "
print(two.isspace()) #True

five = "I love python and"
print(five.islower()) #False

six = "2"
print(six.isidentifier()) #False it is not

seven = "indentefer_1"
print(seven.isidentifier()) #True

x = "sdfasASDFas"
y ="22342ASDFAS"
z = "12212"
print(x.isalpha()) #True
print(y.isalnum()) #True //numbers and alpha characters
print(x.isalpha()) #True
print(z.isalnum()) #True
