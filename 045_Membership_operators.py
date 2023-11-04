#--------------------------
#-----Membership Operators-
#--------------------------
#in 
#not in 

#String
name = 'Assem'
print('s' in name) #True
print('a' in name) #False
print('-'* 50)
#List
friends = ['Assem','Ayman',"Ali"]
print("Assem" in friends) #True
print("assem" in friends) #False
print('assem' not in friends) #True
print('-'*50)

#using In and Not In with condition
countriesOne = ['USA',"Egypt",'KSA']
countriesOneDiscount = 50
countriesTwo = ['Italy','Canda']
countriesTwoDiscount = 10
myCountry = "egypt"

if myCountry in countriesOne:
    print(f'your discounts is is {countriesOneDiscount}')
elif myCountry in countriesTwo:    
    print(f'your discounts is is {countriesTwoDiscount }')
else:
    print("no discount")    