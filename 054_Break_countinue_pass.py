#-----------------------------
#----- Break, Continue, pass--
#-----------------------------

myNumbers = [1,2,3,5,7,10,13,9, 15]
#Cotinue
for num in myNumbers:
    if num == 13:
        continue #stop the current iteration
    print(num)

#Break
for num in myNumbers:
    if num == 13:
        break #stop the loop
    print(num)

#Pass
for i in myNumbers:
    pass     