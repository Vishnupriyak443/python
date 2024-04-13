s1={"abc","xyz",22}
s2={11,22,"abc","ABC"}
set=s1.intersection(s2)
print(set)
for i in set:
    if i in s1:
         s1.remove(i)
print(s1)         
