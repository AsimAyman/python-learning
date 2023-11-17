# --------------------------------
# ----Built in function-----------
# --------------------------------
# abs()
# pow()
# min()
# max()
# slice()

# abs()
print(abs(100))#100
print(abs(-100))#100
print('-'*40)

# pow(base, exp, mod)
print(pow(2,2))#4
print(2**2)#4
print(pow(2,5,2)) #0
print('-'*40)

# min(item,item, item, iterator)
print(min(-2,3,42)) #-2
print(min('z','x',"Osama")) #Osama
print(min((10,301,23,234,12))) #10
print('-'*40)


#slice()

a = ['A','B','C','D']
print(a[:3])           #['A', 'B', 'C']
print(a[slice(3)]) #['A', 'B', 'C']
print(a)