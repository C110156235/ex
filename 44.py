x = int(input("有幾班:"))
y =[]
for i in range(x):
    z = int(input("人數:"))
    y.append(z)
    ans = max(y)
print(ans)