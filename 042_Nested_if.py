#--------------------
#----- Nested If ----
#--------------------

u_Name = "Assem"
u_country ="Egypt"
c_name = "python"
c_price = 100
isStudent= 'Yes'
if u_country == "Egypt" or u_country == "Sudan":
    if isStudent == 'Yes':
        print(f"Hello {u_Name} The course \"{c_name}\" prince is: ${c_price - 95}")
    else:
        print(f"Hello {u_Name} The course \"{c_name}\" prince is: ${c_price - 90}")
elif u_country == "palastain":
    print(f"Hello {u_Name} The course \"{c_name}\" prince is: ${c_price - 90}")
else:
    print(f'you got the global discont {c_discount}')    
    print(f"Hello {u_Name} The course \"{c_name}\" prince is: ${c_price - 30} ")


if u_country == "Egypt" or u_country == "Sudan":
    if isStudent == 'Yes':
        print(f"Hello {u_Name} The course \"{c_name}\" prince is: ${c_price - 95 if isStudent == 'Yes'else 90}")
elif u_country == "palastain":
    print(f"Hello {u_Name} The course \"{c_name}\" prince is: ${c_price - 90}")
else:
    print(f'you got the global discont {c_discount}')    
    print(f"Hello {u_Name} The course \"{c_name}\" prince is: ${c_price - 30} ")
