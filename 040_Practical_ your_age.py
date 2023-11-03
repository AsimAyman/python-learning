#--------------------------------
#------Practical your age full --
#--------------------------------
 
#input age
age =int(input('what is your age? ').strip())
print(type(age))     # from <class 'str'> to be an integer
#get age in all time units

months = age *12
weaks = months *4
days = weaks * 7
hours = days * 24
print('you lived for: ')
print(f"{months} monthes")
print(f"{weaks:,} weaks")
print(f"{days:,} days")
print(f"{hours:,} hours")