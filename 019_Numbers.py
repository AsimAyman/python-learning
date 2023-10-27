#-------------------
#----Numbers--------
#-------------------

#Integer
print(type(1))
print(type(-2))
print(0)

#Float
print(type(1.20032))
print(type(-1212.1))
print(type(0.55))

#Complex
myComplex = 5+6j
print(type(myComplex))
print("Real part is {}".format(myComplex.real))
print("imaginary part is {}".format(myComplex.imag))
# you can convert from int to float or complex
print(100)
print(float(100))
print(complex(100))
# you can convert from float to int or complex
print(100.323)
print(int(100.323))
print(complex(100.323))
# you cna not convert complex to int or float
print(str(myComplex))
