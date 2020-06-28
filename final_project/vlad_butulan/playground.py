from backend import PrittyPrinter, Room, Room_Inventory, Client, Clients
from application import *
import datetime
import yaml

# adding new client with default append() method
client2 = Client(2, {'name':'John', 'surname':'Doe', 'age':'21', 'address':'Necunoscutei 5'}, {})
clients.append(client2)

# adding new client with new_client() method
id = clients.new_client('Bart', 'Simpson', 10, 'Simpsons 90')
print(f"Adding new client via new_client() method. New client id: {id}\n")

# request info for new client
print(f'Client details of id: {id}:\n {clients.get_user(id)}\n')

# client check-in status
for client in clients:
    if client.user_id == id:
        stats = client.status()
print(f'Checking new client status:\n{stats}')

# reserving room for new client
date3 = datetime.date.today()
date4 = date1 + datetime.timedelta(days=5)
print(f"Reserving a room for {clients.get_user(id)}: {room_inventory.reserve('3', id, [date3, date4])}\n")
print(clients.reserve('3', id, [date3, date4]))

print(client1.status())

#demo operator overload
print("using sum operator: room1 + room2\n")
room10 = Room({'nr':1, 'type':'single_room', 'floor':0, 'facilities': ["dishwasher", "toaster"]}, {})
room11 = Room({'nr':2, 'type':'single_room', 'floor':0, 'facilities': ["dishwasher", "TV"]}, {'1':[date3, date4]})
res = room10 + room11
print(res)
