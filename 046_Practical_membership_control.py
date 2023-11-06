#---------------------------------
#---Practical Membership Control--
#---------------------------------

# list of Admins
admin = ['Assem','Ayman','Ibrahem','Ali']
#login
name = input('please input your name ').strip().capitalize()
#if name is in admin
if name in admin:
    print(f'Hello name {name.center(10,"*")} welcome back.')
    option = input("enter 'E' to edit your name,'D' to delet,and 'C' to continue...  ").capitalize().strip()
    #update option
    if option == 'E':
        nw_name = input('Enter the new name ').strip().capitalize()
        admin[admin.index(name)] = nw_name
        print('name is edited')
    #delet option
    elif option == 'D':
        admin.remove(name)
        print('deleted')
    else:
        print('wrong option')     
else:
    status = input(f'do you want to add yourself Y/N ').capitalize().strip()
    if status == 'Y':
        admin.append(name)
        print('you are added')
    else:
        print('you did not added')
print(admin)    