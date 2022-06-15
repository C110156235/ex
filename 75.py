x = []
while True:
    y = input("請輸入事項(若已無事項，請輸入end):")
    x.append(y)
    if y == 'end':
        for i in range(len(x)-1):
            print('%d. %s' %(i+1,x[i]))
        break