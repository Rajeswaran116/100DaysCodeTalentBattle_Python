t=int(input())
for i in range(t):
    w1,w2,x1,x2,m=map(int, input().split())
    w=w2-w1
    xmin=m*x1
    xmax=m*x2
    if w>=xmin and w<=xmax:
        print(1)
    else:
        print(0)