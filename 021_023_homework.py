friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two
print(friends[0])
print(friends[-(len(friends))])
print(friends[-1])
print(friends[4])

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"
print(friends[::2])
print(friends[1::2])


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(friends[1:-1])
print(friends[-2:])


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends[-2:]=['zero','zero']
print(friends)


friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"Nasser")
friends.append('Salem')
# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
print(friends)


friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]
friends = friends[2:]
print(friends)
friends.pop(-1)
print(friends)


friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
allFrinds =[]
allFrinds.extend(friends)
allFrinds.extend(employees)
allFrinds.extend(school)
print(allFrinds)

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
friends.sort()
print(friends)
friends.reverse()
print(friends)

