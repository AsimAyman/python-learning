# ------------------------
# --------Set Methods-----
# ------------------------

#issuperset()
a = {1,2,3,4}
b = {1,2,3}
c = {1,2,2,56,5,565,56}
print(a.issuperset(b)) #True
print(a.issuperset(c)) #False
print('='*50)

#issubset()
d = {1,2,3,4}
e = {1,2,3}
print(d.issubset(e)) #False
print(e.issubset(d)) #True
print('='*50)

#isdisjoint()

f = {1,2,3,4}
g = {1,7,9}
k = {10,55,87}
print(f.isdisjoint(g)) #False
print(g.isdisjoint(k)) #True
print('='*50)
