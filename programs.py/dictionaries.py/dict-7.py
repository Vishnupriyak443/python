sampledict={'emp1':{'name':'pawan','salary':7500},'emp2':{'name':'priya','salary':8000},'emp3':{'name':'raj','salary':500}}
del sampledict['emp3']['salary']
print(sampledict)
sampledict['emp3']['salary']=8500
print(sampledict)