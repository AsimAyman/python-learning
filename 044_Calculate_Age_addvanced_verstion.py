#---------------------------
#-----Calculate Age --------
#collect age data
age = input('Please right your age ').strip()
#collect time data
unit = input("Please choose time unit:(m) Manthos,(w) weeks,(d) days").strip().lower
#get time units

months = age *12
weaks = months *4
days = weaks * 7
hours = days * 24
print('you lived for: '.center(100,"*"))

if unit =="m":
    print('You choosed the unit Monthes')
    print(f'you lived for {months:,} Months.')
elif unit =="w":
    print('You choosed the unit Weaks')
    print(f'you lived for {weaks:,} weaks.')
elif unit =="d":
    print('You choosed the unit days')
    print(f'you lived for {days:,} days.')
else:
    print('Enter a valied input')
