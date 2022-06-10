x=input("輸入值為:")
y=x.split(",")
z=sorted(y)
o=sorted(y,reverse=True)
t1=""
t2=""
for i in range(len(y)):
    t1+=o[i]
    t2+=z[i]
print("最大值數列與最小值數列差值為:%s"%(int(t1)-int(t2)))