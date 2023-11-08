#------------------------
#------loop => For ------
#------Nested loop-------
#------------------------

# people = ['Assem','Ayman','Sayed', 'Ali']
# skills = ['Html','Css','Js']
# for name in people:
#     print(f"{name.center(10,'*')} skills is: ")
#     for skill in skills:
#         print(skill)

people = {
    'Assem':{
        'Html':'35',
        'Css':'33',
        'js':'1',
    },
    'Ayman':{
        'Html':'11',
        'Css':'111',
        'js':'32',
    },
    'Sayed':{        
        'Html':'12',
        'Css':'12',
        'js':'4',}, 
    'Ali':{        
        'Html':'121',
        'Css':'12',
        'js':'43',}
    }
# print(people['Assem']['js'])
# for person in people:
#     print(f"{person} ",)
#     for skill in people[person]:
#          print(f'{skill}=>{people[person][skill]},   ',)
#     print('----------------')
