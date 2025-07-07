my_dict={'rec1':{'name':'Pavan','age':18,'RollNo':123,'mobile':9456782345},}
#this is a hash table using hash table
print(my_dict)
#accessing a specific element
print('Name in rec1:',my_dict['rec1']['name'])
#adding a new element into the dictionary 
my_dict['rec2']={'name':'Alex','age':19,'RollNo':456,'mobile':9456782356}
print(my_dict)
#accessing using loop
for i,j in my_dict.items():
    #it will return the key and values 
    print(i,j)
#now deleting the record from the dictionary
my_dict.pop('rec1')
print('after deleting:',my_dict)
#now deleting a specific record in a rec2
del my_dict['rec2']['mobile']
print(f'after deleting the rec2 of mobile:{my_dict}')
#now updating the record in a dictionary
my_dict['rec2']['age']=100
print(f'after modifying the age in rec2:{my_dict}')