#___________________________________
#---------- Concatenation-----------
# is how to add to strings together
# by using + operator
#___________________________________
msg = "I love"
lang ="python"
full = msg+" "+lang
print(full)

a = "Frist \
Second \
Third"      # Frist Second Third
b = " A \
B \
C"     
print(a+b)    #Frist Second Third A B C
c = a + "\n" + b 
print(c) #Frist Second Third
         # A B C 

#print("one"+ 1) #error: can only concatenate str to str
print("one",1) # one 1
