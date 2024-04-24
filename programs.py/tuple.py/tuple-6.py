#Counting no.of occuraces of an item from a tuple
tup=(10,20,50,30,50,60,70,50)
count=0
for i in tup:
    if (i==50):
        count=count+1
print(count)        