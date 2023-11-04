#--------------------------
#--Ternary Conditional ----
#--------------------------

country = 'Egypt'
if country == 'Egypt': print(f"The weather in {country} is 15")
elif country == "KSA": print(f"The weather in {country} is 30")
else: print(f"the {country} is not in the list")


#short if
print(f"the weather in the {country} is {15 if country=='Egypt' else 'not in the system'}")

movieRate = 18
age = 16

if age < movieRate:
    print("this movie is not for you")
else :
    print("movie is not good for you ")    

# condition if True | if condition | Else | condition if False
print(f'The movie is not good for you i'if age <movieRate else "movie is good for you")
