n=int(input())
l=list(map(int, input().split()))[:n]
ls=set(l)
ll=list(ls)
ll.sort()
print(ll)