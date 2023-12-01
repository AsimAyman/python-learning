#--------------------------------------------------
#----Practical => Loop on many iterators with zep()
#--------------------------------------------------
#zip() Return a zip object contains all objects
#zip() length is the lenght of lowest object
#--------------------------------------------------


list1 =[1,2,3,4,5]
list2 = ['A','B']
tuple1 =('Man','Woman','Girl','Boy')
dic1 = {"name":'Assem','Age':12}

ultimatedList = zip(list1,list2)

print(ultimatedList) #<zip object at 0x0000024212CBC3C0>

for i in ultimatedList:
    print(type(i)) #<class 'tuple'>
    print(i)
    # (1, 'A')
    # (2, 'B')
print('-'*30)

ultimatedList2 = zip(list1,list2)
for tuple_element in ultimatedList2:
    for element in tuple_element:
        print(element)
# 1
# A
# 2
# B

for item1, item2,item3,item4 in zip(list1,list2,tuple1,dic1):
    print('list 1 Item =>',item1)
    print("list 2 Item =>",item2)
    print("tuple 1 Item =>",item3)
    print("dic 1 key =>",item4,"dic 1 value =>",dic1[item4]) # will print only th key 
