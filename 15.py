x=list(input("輸入一組四位數字為:"))
z=[]
for i in x:
    y=(int(i)+7)%10
    z.append(str(y))
o=z[2]+z[3]+z[0]+z[1]
print("輸出加密後的數字為:",o)