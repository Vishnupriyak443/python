ls=['a','e','i','o','u','A','E','I','O','U']
str="VISHNU"
count=0
for i in str:
    if i not in ls:
        count+=1
print(count)        
    