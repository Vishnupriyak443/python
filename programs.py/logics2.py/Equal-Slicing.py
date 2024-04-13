ls=[1,2,3,4,5,6]
l=len(ls)
x=ls[0:2]
y=ls[2:4]
z=ls[4:6]
ls1=x[::-1]+y[::-1]+z[::-1]
print(ls1)