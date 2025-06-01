def passorfail(t):
    for i in range(t):
        a=0
        n,x,p=map(int, input().split())
        a=(x*3)+(x-n)
        if a==p or a>p:
            print("PASS")
        else:
            print("FAIL")
t=int(input())
pf=passorfail(t)    