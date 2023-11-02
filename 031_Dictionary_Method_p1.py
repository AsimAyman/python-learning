#----------------------------
#------Dictionary Methods----
#----------------------------

#clear()
user = {'name':'Assem'}
print(user)
user.clear()
print(user)
print('-'*40)
# {'name': 'Assem'}
# {}

#update()
member = {'name':'Assem'}
member['age']=11
print(member) #{'name': 'Assem', 'age': 11}
member.update({'country':"Egypt"}) 
print(member) #{'name': 'Assem', 'age': 11, 'country': 'Egypt'}
print('-'*40)

#copy()
main = {
    'name':"Osam"
}
b = main.copy()
main.update({'skill':"fighting"})
print(main)
print(b)
# {'name': 'Osam', 'skill': 'fighting'}
# {'name': 'Osam'}
print('-'*40)

#keys(), values()
print(main.keys())
print(main.values())
# dict_keys(['name', 'skill'])
# dict_values(['Osam', 'fighting'])

