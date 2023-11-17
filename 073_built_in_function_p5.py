# --------------------------------
# ----Built in function =>filte---
# --------------------------------
# filter take a function + iterator
# filter run a function on every element
# the function can be predefined functio or lambda funciton 
# filter out all elements for which the function return true
# the function need to retruen boolean value
#---------------------------------

def checkNumber(n):
    return True if n >10 else False
a = [1,2,33,14,50,6,7]
b = filter(checkNumber,a)
print(a)  #[1, 2, 33, 14, 50, 6, 7]
print(list(b)) #[33, 14, 50]
print('-'*40)


def checkName(name):
    return name.startswith('O')

names = ['Osama','Omar','othman','adek']
o_names = filter(checkName,names)
print(list(o_names))
print(list(filter(lambda name:name.startswith('O'),names)))