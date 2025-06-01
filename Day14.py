n=int(input())
if(n==0):
    print("The count of interger is 1")
else:
    while(n!=0):
        r=n%10
        print(r,end="")
        n=n//10
