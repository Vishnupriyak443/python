sampledict={"name":"ABC","age":25,"salary":8000,"city":"Nellore"}
list=["name","salary"]
for i in list:
    if i in sampledict:
        del sampledict[i]
print(sampledict)        
        
