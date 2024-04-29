import json
dict={ }
dict1={} 
n=int(input("Enter no.of books to store in dictionary:"))
n1=int(input("Enter no.of key items:"))
for i in range(0,n):
    key1=input("Enter book number:")
    for i in range(0,n1):
        key=input("Enter a key:")
        value=input("Enter a value:")
        dict1[key]=value
        dict[key1]=dict1
print(dict)
json_string=json.dumps(dict)
print(json_string)