s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
if len(s1)!=len(s2):
    print("This is Not a Anagram")
elif sorted(s1)==sorted(s2):
    print("This is anagram")
else:
    print("This is not a Anagram")

