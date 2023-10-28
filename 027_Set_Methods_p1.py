#------------------------
#--------Set Methods-----
#------------------------

#clear()
a = {1,2,3,4,}
a.clear()
print(a) #set()

#union()
b = {'one','two', 'three'}
c = {1,2,3}
x = {'zero','cool'}
print(b|c) #{1, 2, 3, 'three', 'two', 'one'}
print(b.union(c)) #{1, 'two', 'three', 2, 3, 'one'}
print(b.union(c,x)) #{'zero', 1, 2, 3, 'three', 'cool', 'one', 'two'}

#add()
d = {1,2,3,4}
#d.add(5,6) set.add() takes exactly one argument (2 given) 
d.add(5)
print(d) #{1, 2, 3, 4, 5}
d.add((5,6))
print(d) #{1, 2, 3, 4, 5, (5, 6)}
#d.add([8,9])
#print(d) #TypeError: unhashable type: 'list'

#copy()
e = {1,2,3}
f = e.copy() #shallow copy
e.add(10)
print(e) #{1,2,3,10}
print(f) #{1,2,3} 

#remove()
g ={1,2,3,4}
g.remove(1)
print(g) #{2, 3, 4}
#g.remove(10) KeyError: 10

#discard()
h = {1,2,3,4}
h.discard(1) 
print(h)  #{2, 3, 4}
h.discard(10)
print(h)  #{2, 3, 4}

#pop()
j = {1, 'A',True, 1.2}
#p =j.pop()  # random element
print(j) #{'A', 1.2}
#print(p) #True 

#update() union
k = {1,2,3,4}
l = {1,2,"A","B"}
my_list = ['css','html']
j.update(l)
j.update(my_list)
print(j) #{1, 1.2, 2, 'css', 'html', 'B', 'A'}

 
