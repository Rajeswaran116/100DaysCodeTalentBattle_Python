s=input()
l=['A','E','I','O','U','a','e','i','o','u']
for i in range(len(s)):
    if(s[i] not in l):
        print(s[i], end="")

