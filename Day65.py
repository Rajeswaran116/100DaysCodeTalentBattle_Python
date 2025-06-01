t=int(input())
for i in range(t):
    n,b=map(int, input().split())
    l1=[]
    for i in range(n):
        w,l,p=map(int, input().split())
        if p>b:
            pass
        else:
            a=w*l
            l1.append(a)
    if l1:
        print(max(l1))
    else:
        print("No Tablet")
