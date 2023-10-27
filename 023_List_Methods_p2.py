# ---------------------------
# --------List Methods-------
# ---------------------------

#clear()
a = [1, 2, 4, 4, 5]
a.clear()
print(a)  #[]

#copy
b = [1, 2, 4, 4, 5]
c = b.copy() #shallow copy
b.clear()
print(c)  #[1, 2, 4, 4, 5]
c = b #deep copy
b.append(101)
print(c)

#count
d = [12, 1, 1, 2, 4, 23, 23]
print(d.count(1))  #2
print(d[2:].count(1))  #1
print(d.count(20))  #0


#index
e = [1, 2, 3, 23, 1, 1, 100]
print(e.index(100))  #6 first element
#print(e.index(2002))  #ValueError: 2002 is not in list
print(e.__contains__(2002))  #False

#insert()
f = [1, 2, 3, 1, 1, "12", 12, False]
f.insert(2, "s")
print(f)  #[1, 2, 's', 3, 1, 1, '12', 12, False]
f.insert(-1, "see") #before the index
print(f)

#pop()
g = [1, 2, 3, 100, 10]
p = g.pop(3)
print(g)  #[1, 2, 3, 10]
print(p)  #100
