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
set1.clear() #Clears all elements and results an empty set
print(set1) 
del set #Completely removes a set
print(set)
#Joining sets
st={"ABC","XYZ",123}
st1={2,34,"ABC",}
set2=st.union(st1)
print("Union:",set2)
set3=st|st1
print(st)
set4=st.intersection(st1) #Intersection of two sets and creates a new set
print("intersection",set4)
st.intersection_update(st1) #intersection update >only changes an old set
print(st)
set5=st&st1 #intersection using symbols "&"
print(set5)
set6=st1.difference(st)
print(set6)
set7=st-st1
print(set7) #error
st1.difference_update(st)
print(st1)
set8=st.symmetric_difference(st1)
print(st)