def add(*x):
    print(x)
    sum=0
    for i in x:
        sum=sum+i
    print(sum)    
add(10,20,30) 
add(10,20)
add(10,20,30,40)