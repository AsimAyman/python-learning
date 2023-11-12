# ----------------------------------------------------
# -----Fucntion packing, unpacking Aruments **kWArgs--
# ----------------------------------------------------

# def show_skills(*skills):
# print(type(skill)) #tuple
#     for skill in skills:
#         print(skill)
#

# show_skills('php','js','css')

def show_skills(**skills):  # dictionary
    print(type(skills))  # dict
    for skill, value in skills.items():
        print(f'{skill} => {value}')


show_skills(php=10, js=90, css=12)
my_skills = {
    'html': 12,
    'js': 11,
    'c': 23,
}
show_skills(**my_skills)
