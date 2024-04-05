n=int(input("Enter a number:"))
print(f"Factorial numbers upto {n} values:")
def fact(x):
    i=4
    t1=0
    t2=1
    nextTerm=t1+t2
    print(t1,"\n",t2,"\n",nextTerm)
    while(i<=x):
        t1=t2
        t2=nextTerm
        nextTerm=t1+t2
        print("\n",nextTerm)
fact(n)    