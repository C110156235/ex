s1 = input("請輸入陣列大小:");a=[];b=[];c=0
x=a.append(input().split())
y=a.append(input().split())
z=a.append(input().split())
for i in range(3):
	for j in range(3):
		b.append(int(a[i][j]))
b.sort()
b.reverse()
c=c+b[0]+b[1]+b[2]
print("最大值為:",c)
for i in range(3):
	for j in range(3):
		if str(b[0]) in a[i][j]:
			d=i+1
			e=j+1

		elif str(b[1]) in a[i][j]:
			d2=i+1
			e2=j+1

		elif str(b[2]) in a[i][j]:
			d3=i+1
			e3=j+1
print('位置為:(%d,%d),(%d,%d),(%d,%d)'%(d,e,d2,e2,d3,e3))