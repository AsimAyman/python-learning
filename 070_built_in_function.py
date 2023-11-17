# --------------------------------
# ----Built in function-----------
# --------------------------------

# sum()
# round()
# range()
# print()

# sum(iterable, start)

l = 1, 2, 3, 4, 5

print(sum(l))  # 15
print(sum(l, 100))  # 115
print(sum(l[1:]))  # 14


# round(number, numofdigit)
print(round(150.499))  # 150
print(round(150.499, 1))  # 150,5

# range(start,end ,step)
print(list(range(0)))  # []
print(list(range(10)))  # [1,...,9]

# print()
print('hello osama')
print('hello', 'osama')  # defualt seperator in print is space
print('hello', 'assem', sep='*')

print('first line', end='*')  # end by dafualt is \n
print('second line')
