# ------------------------
# -----User Input---------
# ------------------------
fName = input('what\'s your Frist name? ').strip().capitalize() #chain method
mName = input('what\'s your Middle name? ').strip().capitalize()
lName = input('what\'s your Last name? ' ).strip().capitalize()
print(f"Hello {fName} {mName:.1s}. {lName}")