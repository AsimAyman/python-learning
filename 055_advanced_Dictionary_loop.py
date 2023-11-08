#--------------------------------
#------Advanced Dictionary loop--
#--------------------------------

mySkills={
      'name':200,
      'progress':90}

for skill in mySkills:
    print(f"{skill} => {mySkills[skill]}")

for k,v in mySkills.items():
    print(f'{k} => {v}')  


  
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

for k,v in people.items():
    for c_key,c_value in people[k].items():
        print(f"{c_key} => {c_value}")

        