#---------------------------------
#------While Training-------------
#---------------------------------

myF = ['Ali','Hos','Alaa','Mohamed']
print(myF[0])
print(myF[1])
print(myF[2])
print(myF[3])
print('-'*30)
for i in myF:
    print(i)
print('-'*30)
idx = 0
while idx < len(myF):
    print(f"{str(idx + 1).zfill(2)} ==>>{myF[idx]}")
    idx +=1
print('-'*30)    

