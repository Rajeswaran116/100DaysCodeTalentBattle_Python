n=int(input())
snum=n
count=0
f=1
if(n==0):
    print("Enter another value")
else:
    while(n!=0):
        f=1
        r=n%10
        for i in range(1,r+1):
            f=f*i
        n=n//10
        count=count+f
if(count==snum):
    print("Strong Number")
else:
    print("Not a Strong Number")

