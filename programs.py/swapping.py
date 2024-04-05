print("Before swapping:")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
x=x+y
y=x-y
x=x-y
print("After swapping:")
print("First number:",x)
print("Second number:",y)

p=int(input("P:"))
q=int(input("Q:"))
p,q=q,p
print("P:",p,"\nQ:",q)