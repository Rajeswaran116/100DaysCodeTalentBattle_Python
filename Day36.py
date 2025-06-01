s=input()
a=len(s)-1
for i in range(len(s)):
    if(i==0 or i==a):
        p=s[i].upper()
        print(p,end="")
    else:
        p=s[i]
        print(p,end="")