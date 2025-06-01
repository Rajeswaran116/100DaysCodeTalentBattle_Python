n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
a.sort()
b.sort()
l=[]
for i in range(n):
    c=a[i]*b[i]
    l.append(c)

print(sum(l))
