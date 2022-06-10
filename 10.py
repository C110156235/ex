x=input("輸入N及M為")
y=x.split(" ")
c=[]
d=[]
e=""
f=[]
for i in range(int(y[0])):
    c.append(input("輸入矩陣數值第%d列%s個數字" %(i+1,y[1])))
for j in range(len(c)):
    d.append(c[j].split(" "))
for o in range(int(y[1])):
    for p in range(int(y[0])):
        e+="%s "%(d[p][o])
    f.append(e)
    e=""
for z in range(len(f)):
    print("輸出矩陣數值第%s列為%s" %(int(z)+1,f[z]))