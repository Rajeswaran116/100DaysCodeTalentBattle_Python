n=input()

if(n== 'a' or n== 'e' or n== 'i' or n== 'o' or n== 'u' or n== 'A' or n== 'E' or n== 'I' or n== 'O' or n== 'U'):
    print("Vowel")
elif((n>='A' and n<='Z') or (n>='a' and n<='z')):
    print("Consonant")
else:
    print("Invalid Input")

