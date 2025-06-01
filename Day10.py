
n=int(input())
p=[]
if(n==0):
    print("The Factorial of 0 is o")
else:
    for i in range(1,n+1):
        p.append(i)
        
def multiplyList(myList):
 
    result = 1
    for x in myList:
        result = result * x
    return result

print(multiplyList(p))
