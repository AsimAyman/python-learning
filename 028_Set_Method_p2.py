# ------------------------
# --------Set Methods-----
# ------------------------

# difference
a = {1, 2, 3, 4}
b = {1, 2, 'osama', 'Ahme'}
print(a.difference(b))  # {3, 4}
print(a - b)  # {3, 4}
print('='*50)

# difference_update()
a = {1, 2, 3, 4}
b = {1, 2, 'osama', 'Ahme'}
print(a)  
a.difference_update(b)
print(a)  # {3, 4}
print(b)  # {1, 'Ahme', 2, 'osama'}
print('='*50)

# intersection()
e ={1,2,3,4,'x'}
f ={1,2,3,4,'y'}
print(e.intersection(f)) 
print(e & f) #the same
print(e)
print('='*50)

#intersection_update()
t ={1,2,3,4,'x'}
y ={1,2,3,4,'y'}
print(t)  #{1, 2, 3, 4, 'x'}
t.intersection_update(y)
print(t) #{1, 2, 3, 4}
print(y) #{'y', 1, 2, 3, 4}
print('='*50)

#symetric_difference()
i ={1,2,3,4,5,'x'}
l ={"osama","zero",1,2,4}
print(i)
print(i.symmetric_difference(l)) #i^l
print(i)
print('='*50)

#symmetric_difference_update()
j ={1,2,3,4,5,'x'}
k ={"osama","zero",1,2,4}
print(j) #{1, 2, 3, 4, 5, 'x'}
j.symmetric_difference_update(k)
print(j) #{'osama', 3, 5, 'x', 'zero'}
print('='*50)
