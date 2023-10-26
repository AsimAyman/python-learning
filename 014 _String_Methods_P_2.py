# _____________________________
# -----String Methods----------
# _____________________________
# split()
a = "I love python and php"
print(a.split())  # split by spaces and as elements of list

b = "I-love-python-and-php"
print(b.split(sep='-', maxsplit=2))  # split by spaces and as elements of

c = "I-love-python-and-php"
print(c.rsplit('-', maxsplit=2))  # split by

# center()
e = "Osama"
print(e.center(11, '*'))

# count()  => search for a matching sensitivity and return the count
f = "I love python and php"
print(f.count("php"))  # count
print(f.count("python", 0, 2))  # count start , end optionally

# swapcase()
g = "I love python and php"  # convert the lower case to upercase and vise versa
print(g.swapcase())

# startwith()
h = "I love python and php"
print(h.startswith("I"))  # True case sensitive
print(h.startswith("p", 7, -2))

# endswith()
j = "I love python and php"
print(j.endswith("php"))  # True
print(j.endswith('e', 2, 6))  # True
