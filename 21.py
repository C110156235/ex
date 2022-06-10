f = [["123","Tom DTGD"],["456","Cat CSIE"],["789","Nana ASIE"],["321","Lim DBA"],["654","Won FDD"]]
i = input("輸入查詢學號為:")

for z in range(len(f)):
    if i == f[z][0]:
        print("學生資料為",i,f[z][1])
if i not in f[0] and i not in f[1] and i not in f[2] and i not in f[3] and i not in f[4]:
    print('查詢失敗')
