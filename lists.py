list=["VISHNU","PRIYA",123,0.0023]
list1=["ABC",111]
list[0] #accessing list items
list[0:4] #index range
list[2]=[456,"XYZ"] #adding new item to the list
print(list)
list.append(123) #adding item at end of the list
list.insert(4,"VISHNU") #adding item at the index value
print(list)
list.extend(list1) #adding list1 items to the list at the end
print(list)
list.remove(0.0023) #removing an item directly
print(list)
list1.pop(1) #removing item at index
print(list1)
list3=list1+list #adding two lists
print(list3)
del list3 #completely deleting a list
#print(list3)
print("count= ",list.count("VISHNU")) #gives the count of an item
list2=[23,43,65,87,39,3]
list2.sort()
print(list2.sort(reverse=TRUE))
