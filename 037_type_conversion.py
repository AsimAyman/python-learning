#--------------------------
#------Type converstion----
#--------------------------

#str()
a =10
print(type(a))     #<class 'int'>
print(type(str(a)))#<class 'str'>
b =14.4
print(type(str(b)))#<class 'str'>

s1= '1'
print(type(s1)) #<class 'str'>
print(type(int(s1)))#<class 'int'>

s2 ='asdf'
# print(type(int(s2))) ValueError: invalid literal for int() with base 10: 'asdf'
print('-'*30)

#tuple()
c = 'Osama' #str
d = [1,2,3,4,5] #list
e = {'a','b','c'} #set
f ={'a':1,'b':2}
print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
print(type(tuple(c)))
print(type(tuple(d)))
print(type(tuple(e)))
print(type(tuple(f)))
# ('O', 's', 'a', 'm', 'a')
# (1, 2, 3, 4, 5)
# ('b', 'a', 'c')
# ('a', 'b')
# <class 'tuple'>
# <class 'tuple'>
# <class 'tuple'>
# <class 'tuple'>

a =1 
# print(tuple(a)) TypeError: 'int' object is not iterable
print('-'*40)

#list()
c = 'Osama' #str
d = (1,2,3,4,5) #tup
e = {'a','b','c'} #set
f ={'a':1,'b':2}
print(list(c))
print(list(d))
print(list(e))
print(list(f))
print(type(list(c)))
print(type(list(d)))
print(type(list(e)))
print(type(list(f)))
# ['O', 's', 'a', 'm', 'a']
# [1, 2, 3, 4, 5]
# ['a', 'c', 'b']
# ['a', 'b']
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>
print('-'*50)

#list()
c = 'Osama' #str
d = (1,2,3,4,5) #tup
e = ['a','b','c'] #list
f ={'a':1,'b':2} #map
print(set(c))
print(set(d))
print(set(e))
print(set(f))
print(type(set(c)))
print(type(set(d)))
print(type(set(e)))
print(type(set(f)))
print('-'*50)
# {'s', 'a', 'm', 'O'}
# {1, 2, 3, 4, 5}
# {'a', 'b', 'c'}
# {'a', 'b'} only the keys
# <class 'set'>
# <class 'set'>
# <class 'set'>
# <class 'set'>

#dict()
d = (('1',1),('2',2)) #nested tuple, on dimantion tuple will raise an error 
e = [['a',2],['b',23]] #2 dlist
# f = {{'a',2},{'b',23}} #even 2d set will raise the error since it is unhashaple type set
print(dict(d))
print(dict(e))

print(type(dict(d)))
print(type(dict(e)))

print('-'*50)