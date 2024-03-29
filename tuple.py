tup=(34,54,67,92,43,55,100)
print(tup[4]) #Accessing element by index
print(tup[-5]) # accessing negative indeces
print(tup[1:7]) #range of index
t=("450")  #Treats as string variable >>>it consists only one element
print(type(t)) #Results the type 
ls=list(tup) #converting into lists
print(ls)
ls.append(67)
print(ls)
ls.remove(92)
print(ls)
tp=tuple(ls) #Coverting list to tuple
print("updated tuple:",tp)
(a,b,c,d,x,y,z)=tup #Packing elements 
print(a) #unpacking
print("a=",a,"b=",b,"c=",c)
(x,y,*z)=tp #if No.of variables less than no.of elements >>>>use *
print(z)
(x,*y,z)=tp
print(y)
t=t*2 #prints two times same elments
print(t)
print(tp.count(67))
print(tp.index(67,1,3))
tupl=sorted(tp)
print("Sorted:",tupl)
