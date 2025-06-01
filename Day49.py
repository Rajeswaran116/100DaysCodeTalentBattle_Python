n=int(input())
l1=list(map(int, input().split()))[:n]
l2=list(map(int, input().split()))[:n]
j = -1
b=[]
for i in range(len(l1)):
    a=l1[i]+l2[j]
    b.append(a)
    j=j-1
print(b)
    
