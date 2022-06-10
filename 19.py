a=input("測試的資料量:")
for i in range(int(a)):
    b=input("輸入父母以女的血型空格隔開").split()
    p=[b[0].lower(),b[1].lower()]
    c=b[2].lower()
    if "a" in p and "b" in p:
        print("YES")
    elif "ab" in p and "a" in p or "ab" in p and "b" in p or p[0]==p[1]=="ab":
        if c !="o": print("YES")
        else: print("IMPOSSIBLE")
    elif p[0]==p[1]=="o":
        if c=="o": print("YES")
        else: print("IMPOSSIBLE")
    elif "o" in p and "a" in p or p[0]==p[1]=="a":
        if c=="a" or c=="o": print("YES")
        else: print("IMPOSSIBLE")
    elif "o" in p and "b" in p or p[0]==p[1]=="b":
        if c=="b" or c=="o": print("YES")
        else: print("IMPOSSIBLE")
    elif "o" in p and "ab" in p:
        if c=="a" or c=="b":print("YES")
        else:print("IMPOSSIBLE")