# --------------------------
# ------Boolean-------------
# --------------------------

age =26
country = "Egypt"
rank = 10
print(age > 10)
print(country== 'Egypt')
print('-'*40)

#and
if age >10 and country == 'Egypt' and rank >=10:
    print('You can sign')
print('-'*40)

if age >25 or country == 'Egypt':
    print(True)
print('-'*40)

#not 
print(age >16) #True
print(not age>16) #False