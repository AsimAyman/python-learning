#----------------------------
#------Dictionary Methods----
#----------------------------
#setDefault()
user = {
    'name':'Assem'
}
print(user)
print(user.setdefault("age","32"))
print(user)
# {'name': 'Assem'}
# 32
# {'name': 'Assem', 'age': '32'}  
#if i did not add the secound parameter it will be none
print("-"*30)


#pop()
member = {
    'name':"osama",
    'skill':'php'
}
print(member)
print(member.pop('name'))
print(member)
# {'name': 'osama', 'skill': 'php'}  
# osama
# {'skill': 'php'}
print("-"*30)



#popItem() delete last element
member = {
    'name':"osama",
    'skill':'php'
}
print(member)
member.popitem()
print(member)
# {'name': 'osama', 'skill': 'php'}
# {'name': 'osama'}
print("-"*30)

#itmes()
member = {
    'name':"osama",
    'skill':'php'
}
allItems = member.items()
print(allItems)
member.update({'address':"somewhere"})
print(allItems)
print(type(allItems))
# dict_items([('name', 'osama'), ('skill', 'php')])
# dict_items([('name', 'osama'), ('skill', 'php'), ('address', 'somewhere')])
# <class 'dict_items'>
print('-'*100)


#fromKeys()
a = ('k1','K2','K3')
b = 'v'
print(dict.fromkeys(a,b))
#{'k1': 'v', 'K2': 'v', 'K3': 'v'}