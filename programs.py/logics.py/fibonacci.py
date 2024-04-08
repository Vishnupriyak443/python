def fibonacci(x):
    t1=0
    t2=1
    nextTerm=t1+t2
    print(t1,"\n",t2,"\n",nextTerm)
    for i in range(4,n+1):
        t1=t2
        t2=nextTerm
        nextTerm=t1+t2
        print(nextTerm)
    
n=int(input("Enter n value:"))
print(f"Fibonacci Series up to {n} terms: ")
fibonacci(n)