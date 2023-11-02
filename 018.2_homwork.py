name = 'Assem'
age = '17'
country = 'Egypt'

print(f'"Hello \'{name}\',How You Doing \\ """ Your Age Is "{age}"+And Your country Is {country}')
print(f'"Hello \'{name}\',How You Doing \\ \n""" Your Age Is "{age}"+\nAnd Your country Is {country}')

name = 'Elzero'
print(name[0])
print(name[(len(name)-1)//2])
print(name[len(name)-1])

print(6/2) #3.0
print(6//2) #3

print(name[:3])
print(name[:5:2])
print(name[-1:0:-2])

name = "#@#@Elzero#@#@"

print(name.replace('#@',''))
# Elzero

num = "9", "15","130","950","1500"
print(num[3])
for i in num:
    print(i.zfill(4,))


name_one = "OSamA"
name_two = "osaMA"

# Needed Output
for i in name_one:
    curret_letter = i.lower() if i.isupper() else i.upper()
    print(curret_letter,end='')
print()

for i in name_two:
    print(i.upper() if i.islower() else i.lower(),end='')    
# osAMa
# OSAma
print('-'*30)
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))
# Needed Output
# 

name = "Elzero"
print(name.index('z'))
# Needed Output
# 2


msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace('<3','Love',1))
# Needed Output
# I Love Python And Although <3 Elzero Web School

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3','Love'))

# I Love Python And Although Love Elzero Web School


name = "Osama"
age = 38
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt