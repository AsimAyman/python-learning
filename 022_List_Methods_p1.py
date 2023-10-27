# ---------------------------
# --------List Methods-------
# ---------------------------

# append()
myFrinds = ['Ahmed', 'Osama', 'Sayed']
myOldFrins = ['Ali',"Alaa","Osman"]
myFrinds.append("Assem")
print(myFrinds)
myFrinds.append(12) # you can appand anytype
print(myFrinds)
myFrinds.append(myOldFrins) # it wall add the list as one element [..,..,[]]
print(myFrinds)
print(myFrinds[5][1])  #Alaa

#extend()
a = [1, 2, 3, 4]
b = ['A', 'B', 'c']
a.extend(b)
print(a)

#remove()
x = [1, 2, 3, 4, "Assem", True, 'Assem', 2.3, 'Assem']
x.remove("Assem")
print(x)  #remove the first matching element

# sort()
y = [1, 2,130,100,-10,17] #only integers
y.sort()
print(y)  #[-10, 1, 2, 17, 100, 130]
y.sort(reverse=True)
print(y)  # [130, 100, 17, 2, 1, -10]

# reverse() #reverse the order of the elements
x = [1, 2, 3, 4, "Assem", True] #any type
x.reverse() 
print(x) #[True, 'Assem', 4, 3, 2, 1]