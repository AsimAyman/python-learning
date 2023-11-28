#---------------------------
#------Generators-----------
#---------------------------
# Generator is a funciton with "yield" keyword instead of "return"
# it support iteration and rueturn generator iterator by calling yield
# generator function can have one or more "yield"
# by using next() it resume from where it called "yield" not from begining
# when called, its now start Automatically. its only give you the control
#--------------------------

def myGenerator():
    yield 1
    yield 2
    yield 3

print(myGenerator)  # <function myGenerator at 0x00000258D77704A0>
print(myGenerator()) #<generator object myGenerator at 0x000001207E3389E0>
print(int) #<class 'int'>

myGenerator() # nothing is happed

print("_"* 30)
gen = myGenerator()
print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3v
print("_"* 30)

gen2= myGenerator()
for g in gen2:
    print(g)
print("_"* 30)

for g in myGenerator():
    print(g)    