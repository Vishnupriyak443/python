n=int(input("Enter a number:"))
def fact(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print(f"Factorial of {x} is:{fact}")
fact(n)