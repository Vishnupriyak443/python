s1={"abc",'p',0.003,51,91,"xyz",'32',"ABC"}
s2={"ABC",0.003,'p',91}
for i in s2:
    if i in s1:
        continue
print("Subset")    
for i in s1:
    if i in s2:
        s2.remove(i)
print(s2)
print(s1)