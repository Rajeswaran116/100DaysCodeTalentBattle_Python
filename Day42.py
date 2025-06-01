a=int(input())
b=int(input())
la=list(map(int, input().split()))[:a]
lb=list(map(int, input().split()))[:b]
la.sort()
lb.sort()
count=0
if a==b:
    for i in range(a):
        if la[i]==lb[i]:
            count=count+1        
elif a!=b:
    print("Not Same")
if(count==a):
    print("They are same")
else:
    print("They are Not Same")

