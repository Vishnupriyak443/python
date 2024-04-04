dist={"Name":"Vishnu","Roll.no":"1122"}
print(dist)
dist["DOB"]="21-06-2001"
print(dist)
dist.update({"age":22,"Gender":"Female"})
print(dist)
dist["DOB"]="21-06-2001" #no duplicate key elements
print(dist)
dist.pop("Gender")
print(dist)
dist.popitem() #Removes random elements
print(dist)
del dist["DOB"]
print(dist)
print(dist["Roll.no"])
print(dist.keys())
print("Name:",dist["Name"])
print(dist.values())