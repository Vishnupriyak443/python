def add(name,rno):
    print(f"{name} roll no is {rno}" )
add("Vishnu",1122)    #Keyword only  
add(1122,"Vishnu")

add(rno=1122,name="Priya") #position only
add(name="Priya",rno=1122)
 
def sum(x,y=5): #Default parameter y=0 or y=5 
     print("sum=",x+y)
sum(10)      

def show(*x): #arbitary arguments *arg
    print(x)
show(10)
show(10,20)
show(10,20,30,40,50,60,70,80,90,100)
