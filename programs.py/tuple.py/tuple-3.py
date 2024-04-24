tup=(10,20,30,40,50,60)
(a,b,c,d,e,f)=tup  #PACKING
print("a=",a,"b=",b,"c=",c,"d=",d,"e=",e,"f=",f)
print(d)
(x,y,*z)=tup 
print(z)