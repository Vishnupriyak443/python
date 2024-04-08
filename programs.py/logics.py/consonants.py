str="VISHNU"
vCount=0
cCount=0
for i in  str:
    if(i=='A'or i=='E'or i=='O'or i=='U'or i=='I'or i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
        vCount=vCount+1
    else:
        cCount=cCount+1

print("No.of consonants:",cCount)
    