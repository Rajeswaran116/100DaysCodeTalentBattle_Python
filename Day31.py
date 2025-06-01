s=input()
for i in s:
    if 'A' <= i <= 'Z':
        print(i.lower(), end="")
    elif 'a' <= i <= 'z':
        print(i.upper(), end="")