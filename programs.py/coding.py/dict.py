dict={ }
dict1={} 
n=int(input("Enter no.of elements to store in dictionary:"))
for i in range(0,n):
    key1=input("Enter key value:")
    for i in range(0,n):
        key=input("Enter a key:")
        value=input("Enter a value:")
        dict1[key]=value
    dict[key1]=dict1
print(dict) 

