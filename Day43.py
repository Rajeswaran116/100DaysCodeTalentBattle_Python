n=int(input())
l=list(map(int, input().split()))[:n]
o=0
e=0
m=0
for i in range(n):
    if l[i]%2==0:
        e=e+1
    elif l[i]%2!=0:
        o=o+1

if o==n:
    print("Odd")
elif e==n:
    print("Even")
else:
    print("Mixed")
