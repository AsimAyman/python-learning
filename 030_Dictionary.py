#------------------
#---Dictionary-----
#------------------
# dict itmes are enclosed in curly braces
# dict items is contians key and value
# dict key need to be immutable => (num, string, tupe)list not allowed
# dict value can be any type
# dict key must be uniqe
# dict is not order so you can access it by key not the index
user ={
    'name':'Osama',
    'age' : 12,
    'country': "Egypt",
    (1,2):"one,two",
    #[1,2]:"one,two" TypeError: unhashable type: 'list' 
    1: "one",
    'skills' :['php','Css'],
    1: 'a' #take last key
}
print(user['name']) #Osama
print(user.get('name')) #Osama

key = user.keys()
print(type(key)) #<class 'dict_keys'>
print(user.values()) #dict_values(['Osama', 12, 'Egypt', 'one,two', 'a', ['php', 'Css']])
#print(user)
print('-'*30)

languages = {
    'one':{
        'name':'Html',
        'progress': 80
    },
    'two':{
        'name':'css',
        'progress':90
    },
}
print(languages['one']['name']) #Html
print(len(languages)) #2
print(len(languages['one'])) #2

framworkOne = {
    'name':'ReactJs',
    'progress': 90,
}
framworkTwo = {
    'name':'flutter',
    'progress': 80,
}
framwork ={'one': framworkOne, 'two' :framworkTwo}
print(framwork)
