list=[ ]
n=int(input("Enter no.of elements to store in the list:"))
for i in range(0,n):
        x=input("Enter list elements:")
        list.insert(i,x)
print(list)