#_____________________________
#-----String Methods----------
#_____________________________
print(len("1234")) # bulidin function returns length of elemets in a group
print(len("   123")) # space is counted 

# strip() restrip() lstrip()
a = "    I love python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "###########I love python#########"
print(a.strip('#'))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#@#@#@#@#I love python@#@#@#@#@#@#@#@#@#"
print(a.strip('@#'))

a ="msg I love python the end"
print(a.strip('msg').strip('the end'))


# title() => first letter of every world is capitalized and first letter after the number is capitalized to.
b = 'i Love 2d graphics and 3g techonlogy and python'
print(b.title())

# capitalize() => only first  letter is capitalized
print(b.capitalize())

# upper() => all the word is capitalized
print(b.upper())

# lower() => all the word is lowercase
print(b.lower())

# zfill() => 
c ,d,e= "1","11","100"
print(c.zfill(3) ,d.zfill(3),e.zfill(3))
