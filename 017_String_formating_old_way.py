#________________________________
#---------String Formatting------
#________________________________

# %s => str
# %d => int        +    %(,)
# %f => float             
name = "Assem"
age = 40
rank = 10.2
#print("My name is "+name+" my age is " +age) #can only concatenate str (not "int")
print("My name is %s and my age is %d and my rank is %.1f "%(name,age, rank))

n  = 'Assem'
l = 'python'
y = 10
print('Iam %s, Iam %s with %d years of experience'%(n,l,y))

#Control of the float .f
f_num = 10
print('the number is %f'%f_num) #10
print('the number is %f'%f_num) #10.000000
print('the number is %.3f'%f_num) #10.000

# Truncate String
my_long_str = 'Hello student op python i will be the best'
print("the massage is %s"%my_long_str) #the massage is Hello student op python i will be the best
print("the massage is %.5s"%my_long_str) #the massage is Hello

