t=int(input())
for i in range(t):
    m,h=map(int, input().split())
    s=m/(h*2)
    if s<=18:
        print(1)
    elif s>=19 and s<=24:
        print(2)
    elif s>=25 and s<=29:
        print(3)
    else:
        print(4)