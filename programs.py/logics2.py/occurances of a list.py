ls=["abc",10,60,30,"xyz",10,30,"abc"]
count=0
ch=ls[4]
for i in ls:
    if(i==ch):
        count=count+1
print(f"{ch} is occured {count} times in the list")




