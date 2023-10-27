# -------------------------
# ---------Lists-----------
# -------------------------
# List is items are enclosed in square brackets
# List is ordered, to use index to access itme
# list is Mutable => add, delete, edit
# list itmes is not unique
# list cna have different data types
myAwesomeList = [1, "two", True, 2.4, 5, 5]
print(myAwesomeList)  # [1, 'two', True, 2.4, 5, 5]
print(myAwesomeList[1])  # two
print(type(myAwesomeList[1]))  # str
print(myAwesomeList[-1])  # 5
print(myAwesomeList[-4])  # True
# print(myAwesomeList[100])  #IndexError: list index out of range
print(myAwesomeList[0:4])  # [1, 'two', True, 2.4] end is not included
print(type(myAwesomeList[0:4]))
print(myAwesomeList[1:-2])  # ['two', True, 2.4]
print(myAwesomeList[1:])  # ['two', True, 2.4, 5, 5]
print(myAwesomeList[0::2])  # [1, True, 5]

print(myAwesomeList)
myAwesomeList[0] = 10355
print(myAwesomeList)
myAwesomeList[0:3] = []
print(myAwesomeList)
# myAwesomeList[0:3] = 0 # error
myAwesomeList[0:3] = [1, 2, 3]
print(myAwesomeList)  # [1, 2, 3]
myAwesomeList[0:3] = [1,]
print(myAwesomeList)  #[1]

myAwesomeList = [1, 2, 3, 4, 5, 6, 7] 
print(len(myAwesomeList)) #7
print(myAwesomeList.index(myAwesomeList[-1])) #6
