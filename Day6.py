a,b= map(int, input().split())
if(a>=0 and b>=0):
    print("Q1")
elif(a>=0 and b<0):
    print("Q4")
elif(a<0 and b<0):
    print("Q3")
else:
    print("Q2")