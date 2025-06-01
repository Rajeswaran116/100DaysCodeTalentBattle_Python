n=int(input())
l=list(map(int, input().split()))[:n]
l.sort()
print(" The smallest element array:",l[0])
print("The Highest element array: ",l[-1])