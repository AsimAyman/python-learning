# -------------------------------------
# ------Date and time => introduction--
# -------------------------------------

import datetime
for e in dir(datetime):
    print(f'=>{e}')

print('-'*30)
print(dir(datetime.datetime))
print('-'*30)

print(datetime.datetime.now()) #2023-11-19 21:00:20.806062
print('-'*30)

# help(datetime.datetime.now())
print('-'*30)

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().day)
print(datetime.datetime.now().time()) #21:06:43.522279

#print start and end of date
print(datetime.datetime.min)
print(datetime.datetime.max)


#print specific date
print(datetime.datetime(1996,10,10))


print(datetime.datetime(1998,2,3) - datetime.datetime.now())
print((datetime.datetime(1998,2,3) - datetime.datetime.now()).days)
