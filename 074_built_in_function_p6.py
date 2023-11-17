# --------------------------------
# ----Built in function => reduce-
# --------------------------------
# reduce take a function + iterator
# reduce run a function on first and second element and give result
# then run function on result and third element
# then run function on result and fourth element and so on 
# till one element is left and theis is the result of the reduce
# the function can be predefined function or lambda function
#----------------------------------


def sumAll(num1,num2):
    return num1 +num2
a = [1,2,3,4,5,6,7]
s = "a",'b','c','d'
from functools import reduce
result = reduce(sumAll,a)
print(result)  #28
result = reduce(sumAll,s)
print(result) #abcd



