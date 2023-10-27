# -------------------------------
# -------- Tuples----------------
# -------------------------------
# Tuple items are enclosed in parentheses
# you can revove the parentheses
# tuple are ordered, so you use index to access itmem
# tuple are immutable, you can not add or delete
# tuple is not unique
# you can use data type
# Methods used in string and in list  is available with tuple
t1 = ("Assem", "Ayman")
t2 = "Assem", "Ayman"
print(t1)  # ('Assem', 'Ayman')
print(t2)  # ('Assem', 'Ayman')
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# tuple indexing
t3 = 1, 2, 3, 4, 5, 6
print(t3)
print(type(t3))  # <class 'tuple'>
print(t3[1])  # 2
print(t3[-2])  # 5
print(t3[2:-1])  # (3,4,5)

t4 = (1, 2, 3, 4)
#t4[2]="Three" TypeError: 'tuple' object does not support item assignment
