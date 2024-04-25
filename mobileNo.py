num="8985235014"
int=(map(int,num))
ls1=list(int)
ls=[]
for i in range(0,10):
    if i not in ls1:
        ls.append(i)
print(ls)        


