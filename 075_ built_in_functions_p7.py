# --------------------------------
# ----Built in function =>--------
# --------------------------------
# enumerate()
# help()
# reversed()
# -------------------------------

# enumberate(iterable, start =0)
# myskills =['html','css','js','php']
# for skill in myskills:
#     print(skill)
# print('-'*40) 

# myskills_with_counter = enumerate(myskills)
# print(type(myskills_with_counter)) #<class 'enumerate'>
# for sc in myskills_with_counter:
#     print(sc) #(0, 'html') ....
# print('-'*40) 

# myskills_with_counter = enumerate(myskills)
# for c,s in myskills_with_counter:
#     print(f'{c} => {s}') 
# print('-'*40) 

# # help()
# print(help(print))
# print('-'*40)

# reversed(iterrable)
mystring = "Assem"
reversed_string = ''.join(reversed(mystring))
print(reversed(mystring))

