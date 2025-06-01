n=int(input())
l=[]
for i in range(n):
    t,x=map(int, input().split())
    if t==1:
        l.append(x)
    elif t==2:
        l.remove(x)
    elif t==3:
        if x in l:
            print("Yes")
        else:
            print("No")

