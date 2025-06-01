n=int(input())
l=list(map(int, input().split()))[:n]
m=[]
for i in range(len(l)):
    c=l[i]*l[i]
    m.append(c)

print(sum(m))
