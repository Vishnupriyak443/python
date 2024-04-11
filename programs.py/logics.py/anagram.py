s1="cat"
s2="act"
s1=list(s1)
s2=list(s2)
s1=sorted(s1)
s2.sort()
if(s1==s2):
    print("Anagram")
else:
    print("Not an Anagram")