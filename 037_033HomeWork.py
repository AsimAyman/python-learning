# في أول 4 أسطر وبإستخدام Bool Method قم بطباعة 4 أنواع بيانات مختلفة نتيجتهم هي True
# في السطر الخامس إلى الثامن وبإستخدام Bool Method قم بطباعة 4 أنواع بيانات مختلفة نتيجتهم هي False
# # Needed Output
# True
# True
# True
# True
# False
# False
# False
# False
print(bool(True))
print(bool(1))
print(bool(23*2))
print(bool(1<2 and 1 >0))
print(bool (1<0 or 1<-2 or 1<=1))
print('-'*40)

# قم بإنشاء 3 متغيرات فيهم أسماء أي مهارات برمجية تمتلكها والقيمة الخاصة بهم هي نسبة تعلمك لهذه المهارات وتكون كلها فوق 50%
# في سطر واحد فقط وبواسطة ال Boolean Operators قم بالتأكد أن نسبة تعلمك في جميع المهارات أكبر من 50%
# يجب عدم إستخدام If Condition هنا ويجب إرجاع النتيجة True

html = 80
css = 60
javascript = 70
print(bool(html>50 and css> 50 and javascript>50))
print('-'*40)
# Needed Output
# True

# قم بإنشاء متغير بإسم num_two والقيمة الخاصة به هي رقم 20
# قم بإنشاء متغير ثالث بإسم num والقيمة الخاصة به هي رقم 20
# في السطر الأول قم بطباعة نتيجة فحص إذا كان المتغير num أكبر من واحد من المتغيرين الآخريين فقط وليس الإثنين
# في السطر الثاني قم بطباعة نتيجة فحص إذا كان المتغير num أكبر من المتغيرين الآخريين أم لا
num_one = 10
num_two = 20
num = 20
print(num > num_one or num> num_two)
print(num > num_one and num> num_two)

# # Needed Output

# True
# False




# قم بإنشاء متغير باسم num_one والقيمة الخاصة به هي رقم 10
# قم بإنشاء متغير بإسم num_two والقيمة الخاصة به هي رقم 20
# قم بتخزين نتيجة جمع المتغيريين في متغير جديد بإسم result وقم بطباعته في السطر الأول
# في السطر الثاني قم بإيجاد نتيجة رفع الرقم لل Exponent 3
# في السطر الثالث قم بإيجاد باقي قسمة الرقم الناتج من الطلب السابق على 26000
# في السطر الرابع قم بطباعة نتيجة قسمة الرقم الناتج على 5
# تأكد أن الرقم السابق عبارة عن Float لتعرف أنك وصلت للحل بشكل سليم
# في السطر الخامس قم بطباعة النوع بعد تحويله ل String للتأكد من أنه String
num_one = 10
num_two = 20
result = num_two + num_one
print(result)
resultEx = result **3
print(resultEx)
resultRem = resultEx %26000
print(resultRem)
resultRem5 = resultRem/5
print(resultRem5)
print(type(resultRem5))
print(type(str(resultRem5)))

