n=int(input())
a=0
b=1
count=0
print(a,b,end=',')
for i in range(2,n):
    count=a+b
    print(count,end=',')
    a=b
    b=count