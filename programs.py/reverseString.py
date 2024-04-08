def reverse(s):
    str = " "
    for i in s:
        str=i+str
    return str       
s="CODE AVENUE"
print("Before:",s) 
print("After:",reverse(s)) 