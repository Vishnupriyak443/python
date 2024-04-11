def char(c,st):
    count=0
    for i in st:
        if (i==ch):
            count=count+1
    return(count)

str="Vishnu priya"
ch=input("Enter a character:")
print("No. of Occurances of a character {ch} is: ",char(ch,str))

