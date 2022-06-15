x = int(input("輸入一正整數:"))
if x % 2 == 0 and x % 11 == 0:
    if x % 5 != 0 and x % 7 != 0:
        print("%d為新公倍數?:Yes" % (x))
else:
    print("%d為新公倍數?:No" % (x))