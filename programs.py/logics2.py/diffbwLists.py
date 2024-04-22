ls1=[10,20,30,'a','b','c',"xyz"]
ls2=["abc",10,30,20,"xyz",0.003]
for i in ls1:
    if i not in ls2:
        print(i)        