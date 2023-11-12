# ------------------------
# ----Function Scope------
#-------------------------

x = 1

def one():
    x= 2
    print(f"print varibale from function scope {x}")
    print(z)

def two():
    # global x to make x global
    global z
    z  = 10
    x= 4
    print(f"print varibale from function scope {x}")

two()
print(f"print variable from global scope {x}") #1
one()#2