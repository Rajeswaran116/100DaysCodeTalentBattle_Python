def palindrome_array():
    n=int(input())
    l=list(map(int, input().split()))[:n]
    pl=[]
    for i in range(n):
        rem=0
        count=0
        n=l[i]
        while n!=0:
            r=n%10
            rem=rem*10+r
            n=n//10
        if rem==l[i]:
            pl.append(rem)
    print(max(pl))




pa=palindrome_array()