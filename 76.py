b=''
x = input('傳送密碼(6位數)')
while len(x)!=6:
    print('請輸入六位數密碼')
    x = input('傳送密碼(6位數)')
for j in x:
    for i in range(1,10):
        if i*4%7 == int(j):
            b+=str(i)
            break
print('解密後的密碼:',b)