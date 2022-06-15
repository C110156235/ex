x = ["國文","英文","微積分","體育","程式設計"]
y = []
for i in range(len(x)):
    y.append(int(input(x[i]+":")))
print("平均分數:%.2f分" %(sum(y)/len(x)))
print("最高分科目：" + x[y.index(max(y))],max(y),"分")
print("最低分科目：" + x[y.index(min(y))],min(y),"分")