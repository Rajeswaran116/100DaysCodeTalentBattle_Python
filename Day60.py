t=int(input())
for i in range(t):
    o=0
    z=0
    a=list(map(int, input().split()))
    for i in range(len(a)):
        if a[i]==0:
            z=z+1
        elif a[i]==1:
            o=o+1
    if o>z:
        print("Yes")
    else:
        print("No")


