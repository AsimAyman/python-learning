# -------------------------------
# -------- Tuples----------------
# -------------------------------

#Tuple with one element
t1 =("Assem")
print(type(t1)) #<class 'str'>

t2 =(tuple)("Assem")
print(type(t1)) #<class 'tuple'>

t3 ="Assem",
print(type(t3)) #<class 'tuple'>

#tuple concatunation
a = (1,2,3,4,5,6)
b = 7 ,8
c = a + b
print(c) #(1, 2, 3, 4, 5, 6, 7, 8)

#tuple ,list , string REPEAT *
d = (1,2,3,4,5,6) #(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)        
e = ['a','b','c'] #['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
f = 'Assem'       #AssemAssemAssem
print(d * 3)
print(e * 3)
print(f * 3)

#count()
g = (1,2,2,3,3,52)
print(g.count(2)) #2

#index()
h = (1,2,3,4,5,100)
#print("the postion of index is: " + h.index(100))  TypeError: can only concatenate str (not "int") to st
print("the postion of index is: {}".format(h.index(100))) #the postion of index is: 5
print(f"the postion of index is: {h.index(100)}") #the postion of index is: 5


#Tuple Destruct
a = ("A","B","Z")
x, y, z = "A","B","Z"
q,w , e = a # is the same
y,_,u = a # to ignore one elemet


