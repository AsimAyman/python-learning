#-------------------------
#----Loop => For ---------
#-------------------------
# for item in iterable_object:
#     do somthing with item
#-------------------------

myNums = [1,3,4,5,6,6,7,8,8,7]

for num in myNums:
    if num %2==0 :
        print(f'{num} is Even num')
    else :
         print(f'{num} is Even odd') 
else:
    print("loop is finished")        

myName = 'Osama'
for letter in myName:
    print(f"=>>>>>{letter}")     


