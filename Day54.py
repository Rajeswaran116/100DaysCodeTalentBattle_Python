n1=int(input())
n2=int(input())
l1=list(map(int, input().split()))[:n1]
l2=list(map(int, input().split()))[:n2]
a=len(l1)
b=len(l2)
count=0
if(a>b):
    for i in range(len(l1)):
        if l1[i] in l2:
            count=count+1
        else:
            pass
if(b>a):
    for i in range(l2(len)):
        if l2[i] in l1:
            count=count+1
        else:
            pass

if count==0:
    print("Disjoint")
else:
    print("joint")
