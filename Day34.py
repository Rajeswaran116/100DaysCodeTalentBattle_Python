n=input()
l=['(',')']
for i in range(len(n)):
    if(n[i] not in l):
        print(n[i],end="")