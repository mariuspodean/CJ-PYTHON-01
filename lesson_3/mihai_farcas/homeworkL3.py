#Homework
#1.0.9 !Homework!:Two list methods are not listed here.
#Using the python documentation find out the missing methodsand play with
#then in order to figure out what they do
cars = ['Audi', 'Toyota', 'Mazda','Dacia','Renault','Bmw']

#1'st method = list.sort
print('the 1\'st method----sort()')
print('initial value of cars: ')
print(cars)
cars.sort()
print('value of cars after sort()')
print(cars)


#2 method = list.reverse
print('\n the second method-- reverse()')
cars = ['Audi', 'Toyota', 'Mazda','Dacia','Renault','Bmw']
print('initial value of cars: ')
print(cars)
cars.reverse()
print('value of cars after reverse() method')
print(cars)

#3 method = list.copy
print('\n the 3 method-- copy ()')
cars = ['Audi', 'Toyota', 'Mazda','Dacia','Renault','Bmw']
print('initial value of cars: ')
print(cars)
copy_of_cars= cars.copy()
print('value of copy_of_cars after cars.copy() method')
print(copy_of_cars)

#4 Mimic the behaviour of append() by using insert()
print('\n Mimic the behaviour of append() by using insert()')
cars = ['Audi', 'Toyota', 'Mazda','Dacia','Renault','Bmw']
print('initial value of cars: ')
print(cars)
cars.insert(len(cars)+1,'Logan')
print('value of cars after mimic the behavior of append() by using insert()')
print(cars)

#5 Hobby shop
print('\n Hobby shop')
prod=[(types,size) for types in ('shirt','scarf', 'glove','heat') for size in ('S', 'M', 'L', 'XL', 'XXL')] *20
#sell the last item added
print('This is the last item and we will sell it:'+ str(prod.pop(len(prod)-1)))
print('This is the list without the item sold: '+str(prod))
#sell any item from the shop
#sell the item with the index =3
print('Sell the item with index=3')
prod.pop(3)

#sell the 1'st item (glove, XL) from the list of items
print("Sell the first item ('glove', 'XL')")
prod.remove(('glove','XL'))

#restock with new items, add a item @end 
prod.append(('scarf','M'))
print("\n List with ('scarf','M') added at the end" ) 
print(prod)

prod.insert(13,('shirt','S'))
print("\n List with ('shirt','S') added on index 13" ) 
print(prod)