import json
list=[]
dict={'Book':'','author':'','price':''}
n=int(input("Enter n value:"))
for i in range(0,n):
    b=input("Enter book name:")
    a=input("Enter author name:")
    p=input("Enter price:")
    x={'book':b,'author':a,'price':p}
    list.append(x)
json_string=json.dumps(list,indent=4)
print(json_string)
decode=json.loads(json_string)
print(decode)