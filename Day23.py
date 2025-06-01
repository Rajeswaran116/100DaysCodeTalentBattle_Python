n=int(input())
st=str(n)
for i in range(0,len(st)):
    if(st[i]=="0"):
        print("1",end='')
    else:
        print(st[i],end="")