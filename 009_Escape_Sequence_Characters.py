#____________________________________
# Escape Sequences Characters
# \b => Backspace
# \ => Escape newline + \
# \' => Escape Quote
# \t => add Tab
# \n => new feed
# \r => Carraige Return
# \xhh => Character Hex value
#____________________________________
print("Asse\bm") #Assm
print(""" Hello \ 
I love python  
""") # Hello I love python
print("I love \\") #I love \
print("I love \t python") #I love    python
print("I love \n python") # I love 
                          # python
print("1234567\rAssem")   # Assem67  
print("\x4f")   # O         


