x=int(input("請輸入階乘值M:"))
y=0
t=1
while x>t:
    y+=1
    t*=y
print("超過M為1000的最小階層N值為:",y)