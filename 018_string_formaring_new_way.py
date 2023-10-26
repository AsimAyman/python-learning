#________________________________
#---String Formatting New Way----
#________________________________
#"{place holder}{placeholder}".format(var1, var2)
name = "Assem"
age = 40
rank = 10.123456
print("My name is {} and my age is {} and my rank is {} ".format(name, age, rank))
print("My name is {:s} and my age is {:d} and my rank is {:f} ".format(name, age, rank))

#  Controal of floating point
print("My name is {:s} and my age is {:d} and my rank is {:.2f} ".format(name, age, rank))

# Truncate string
my_long_str = 'Hello student op python i will be the best'
print("the massage i {:.5s}".format(my_long_str)) #Hello

# format of money   
myMoney =23423432423
print("My money is {:_}".format(myMoney))  #My money is 23_423_432_423
print("My money is {:,}".format(myMoney))  #My money is 23,423,432,423

# ReArrange Items
a, b, c =1, 2, 3
print("hello {2} {1} {0}".format(a, b, c)) #hello 3 2 1
print("hello {2:d} {1:d} {0:.1f}".format(a, b, c)) #hello 3 2 1.0

# Format in ver 3.6
myName ="Assem"
myage =23

print(f"my name is {myName}, and my age is {myage}") 
# important webset for formatting https://pyformat.info/

