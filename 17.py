sum=[]
ans=''
a1=input("")
b1=a1.split(" ")
c1=[]
d1=[]
for i in range(int(b1[0])):
    c1.append(input(""))
for j in range(len(c1)):
    d1.append(c1[j].split(" "))

a2=input("")
b2=a2.split(" ")
c2=[]
d2=[]
for i in range(int(b2[0])):
    c2.append(input(""))
for j in range(len(c2)):
    d2.append(c2[j].split(" "))

if b1[0]==b2[0] and b1[1]==b2[1]:
    for x in range(len(c1)):
        for y in range(len(d1)):
            sum.append(str(int(d1[x][y])+int(d2[x][y])))
    ans=sum[0]+' '+sum[1]+'\n'+sum[2]+' '+sum[3]
    print(ans)
else:
    print("兩陣列不能相加")