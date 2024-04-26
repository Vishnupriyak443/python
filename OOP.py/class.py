#creating class in python
class Addition:
    classVariable1=10 #class variable declaration
    classVariable2=20
    def __init__(self,x,y): #Constructor method
        self.x=x #instance variable
        self.y=y
    def show(self):  #instance method
        print("x=",self.x)
        print("y=",self.y)
    def sum(self):
        print("sum :",self.x+self.y)       
obj=Addition(3,5)
print("accessing instance variables: \nx=",obj.x)
print("y=",obj.y)
obj.show()      #Calling methos using object
obj.sum()
print("Accessing Class variable: \n1-",Addition.classVariable1,"\n2-",Addition.classVariable2) #Accessing class variables



