#----------------------
#-----Loop =>for-------
#-----Traingings-------
#----------------------

# loop with range
# myRange = range(1,100)
# for num in myRange:
#     print(num) #99

#dictionary
mySkills = {"html":90,'Css':12,'php':13}
print(mySkills['Css'])
print(mySkills.get('php'))
print('-'*39)
for skill in mySkills:
    # print(skill) #will add only the kies
    print(f'{skill} ==>>{mySkills[skill]}')