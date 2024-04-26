tup=( )
ls=list(tup)
n=int(input("Enter no.of elements to store in tuple:"))
for i in range(0,n):
    x=input("Enter tuple elements:")
    ls.insert(i,x)
tuple=tuple(ls)
print(tuple)    