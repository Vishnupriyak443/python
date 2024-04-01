set={20,30,40,50,40}
set1={"ABC","abc","XYZ"}
list=["XYZ",123] #lists
tuple=('a','b')
print(set)
set.add(20) #adding element
print(set)
set.add(44)
print(set)
set.update(set1)
print("After adding another set:",set)
set.update(list) #Adding list to the set
print("After adding with lists:",set)
set.update(tuple)
print("After updating with tuple:",set)
set1.remove("abc") #Removing elements
print(set1)
set.discard(44)
print(set)
set.pop() #Removes Randon element
print(set)
set1.pop()
print(set1)
print("Union: ",set.union(set1))
print("intersection:",set.intersection(set1))




set1.clear() #Clears all elements and results an empty set
print(set1) 
del set #Completely removes a set
print(set)
