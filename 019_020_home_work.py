print(type(1))
print(type(2.2))
print(type(1+2j))
# <class 'int'>
# <class 'float'>
# <class 'complex'>

n = 1+2j

print('{:}'.format(n.imag))
print('{:}'.format(n.real))
# Print Imaginary Part Here
# Print Real Part Here

num = 10
print("{:.10f}".format(num))
# Needed Ouput
# 10.0000000000

num = 159.650

print(int(num))
print(type(int(num)))
# Needed Output
# 159
# <class 'int'>