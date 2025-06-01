n=int(input())
count=0
while(n!=0):
    r=n%10
    count=count+r
    n=n//10

print(count)
    