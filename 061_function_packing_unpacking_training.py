#---------------------------------------------
#------Function Packing, unpacking Arguments--
#---------------------------------------------

def show_skills(name,*skills,**skills_with_prog):
    print(f'hello {name}')
    print(f"skills without progress is :")
    for skill in skills:
        print(skill)
    for k,v in skills_with_prog.items():
        print(f'{k} {"=>".center(10," ")} {v}')   

skillsProg = {
    'c++': 100,
    'c':90
}
show_skills("ahmed")
show_skills('Osama','html','css','js',**skillsProg)    
