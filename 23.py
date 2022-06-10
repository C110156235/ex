x = int(input("輸入值n為:"))
if x == -1 :
    pass
elif 0<x<=100:
    print(round(x**3 / 3,1))
else:
    print('輸入100內的正整數')