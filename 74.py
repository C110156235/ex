ans = ['red','blue','red','green']
n = 10
for i in range(10):
    x = (input('輸入四個顏色(中間以空白隔開)'))
    y = x.split() 
    t = ""
    if len(y) ==4: 
        for z in range(4):
          if ans[z]==y[z]:
            t+='1'
          elif y[z] in ans:
            t+='2'
          else:
            t+='3'
        print(t)
        if t=='1111':
          print('正確答案')
          break
        else:
          print('你還有%s次機會'%(n-1))
          n-=1
    else:
      print('請輸入正確')
    if n == 0:
      print('挑戰失敗')