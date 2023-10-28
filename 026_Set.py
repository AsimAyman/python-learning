#------------------------
#--------Set-------------
#------------------------
#set items are encloesd in Curly Brackes
#set items are Not orderd and Not indexed
#set indexing and slicing can be done
#set has only immutable type (Number, String,Tuples) List and Dict are not
#Items is unique //True and 1 is the considered as the same element


s1 = {1, 2,3, 3, 4, 5, 6}
print(type(s1))  # <class'set'>
print(s1) # {1, 2, 3, 4, 5, 6}
# print(s1[2]) TypeError: 'set' object is not subscriptable

t  = (1, 2, 3,)
s2 = {1, 2, 3,4}
print(t[:3])
#print(s2[:3]) TypeError: 'set' object is not subscriptable

s3={1,2,3,"asdf",True,(1,3,4)}
s4 ={[1,3,3],{"name":"assem"}}
print(s3)
# print(s4)  typeError unhashable type

