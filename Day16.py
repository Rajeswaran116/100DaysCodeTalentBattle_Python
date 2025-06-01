n=int(input())
p=[]
for i in range(1,n):
    if(n%i==0):
        p.append(i)

sp=sum(p)
if(sp==n):
    print("Perfect")
else:
    print("Not Perfect")