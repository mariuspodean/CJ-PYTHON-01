Create a program to monitor work orders for a auto workshop.

data to be processed:
 - work order
 - registration number of car
 - vin (vehicle identification number)
 - car brand
 - car type
 - client
 - entry date
 - release date
 - labor hours
 - auto parts cost
 - labor cost
 - total cost

primary input data (at the opening work order):
 - registration number of car
 - vin (vehicle identification number)
 - car brand
 - car type
 - client
system data:
- entry date (at the opening work order)
- release date (at the closing work order)

last input data (at the closing work order):
- labor hours
- auto parts cost

automatically generated data:
- work order number
- labor cost
- total cost 

features:
- opening a work order
- add the new work order in open work orders database
- close a work order , delete from open work orders database and add to closed work orders database
- ensure that all the necessary data are in when a work order is closed
- ensure that any work order closed can not be deleted
- display all the open / closed work orders 
- check if a car has open / closed work orders (by registration number) , display it / them , and calculate all costs
- check if a client has open / closed work orders (by registration number) , display it / them , and calculate all costs
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2NDQ0MDI0Nl19
-->