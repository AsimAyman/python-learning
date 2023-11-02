#قم بإنشاء Tuple مكونة من عنصر واحد وليكن إسمك بدون إستخدام الأقواس () ثم قم بطباعة العنصر الوحيد في ال Tuple في السطر الأول وفي السطر الثاني قم بطباعة النوع لتتأكد ان النوع Tuple
# Needed Output
# "Osama"
# <class 'tuple'>
t = "assem",
print(t)
print(type(t))


#قم بإنشاء Tuple تحتوي على أسماء 3 من أصدقاءك وأول إسم يكون Osama
#إستخدم خبرتك وما تعلمته سابقا لتغيير أول إسم من Osama إلى Elzero
# قم بطباعة محتوى ال Tuple في السطر الأول
# قم بطباعة النوع للتأكد من أنه Tuple وليس نوع بيانات آخر
# في السطر الثالث قم بطباعة عدد العناصر داخل ال Tuple
friends = ("Osama", "Ahmed", "Sayed")
# Needed Output
# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
list_of_frinds =list(friends)
list_of_frinds[0] ="Elzero"
friends = tuple(list_of_frinds)
print(friends)
print(type(friends))




# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements

# قم بإنشاء Tuple تحتوي على الأرقام من 1 إلى 3
# قم بإنشاء Tuple تحتوي على الحروف من A إلى C
# قم بعمل Concatenate لهم في Tuple جديدة وقم بطباعة محتواها في السطر الأول
# في السطر الثاني قم بحساب عدد العناصر الموجودة داخل ال Tuple الجديدة
nums = (1, 2, 3)
letters = ("A", "B", "C")
# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
new_tuple= nums +letters
print(new_tuple)

my_tuple = (1, 2, 3, 4)
a,b,c,d = my_tuple
print(a)
print(b)
print(c)
print(d)
# Needed Output

# 1
# 2
# 4