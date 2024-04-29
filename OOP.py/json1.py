import json
dict={}
n=int(input("Enter no.of books to store in dictionary:"))
for i in range(0,n):
    key=input("Enter a key:")
    value=input("Enter a value:")
    dict[key]=value
print(dict)
#json_string=json.dumps(dict)
#print(json_string)