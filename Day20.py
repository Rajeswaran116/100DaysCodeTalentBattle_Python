n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1

if(count==2):
    print("Prime Number")
else:
    print("Not Prime Number")