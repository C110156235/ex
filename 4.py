x=int(input("輸入x座標"))
y=int(input("輸入y座標"))
d=x**2+y**2
if x>0 and y>0:
    print("該點位於第一象限，距離原點為根號%d"%(d))
elif x<0 and y>0:
    print("該點位於第二象限，距離原點為根號%d"%(d))
elif x<0 and y<0:
    print("該點位於第三象限，距離原點為根號%d"%(d))
elif x>0 and y<0:
    print("該點位於第四象限，距離原點為根號%d"%(d))
elif x==0 and y!=0:
    print("該點位於y軸上，距離原點為根號%d"%(d))
elif x!=0 and y==0:
    print("該點位於x軸上，距離原點為根號%d"%(d))
else:
    print("該點位於原點")