from random import choice
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

# in_use = {'user_id':[check_in, check_out], 'user_id':[check_in, check_out]}

class My_Rooms_CM():

    def __enter__(self):
        self.file = open('rooms.yaml')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


class PrittyPrinter():
    """a mixin class used by Room and Client to print nicely their contents"""
    
    def pp_print_recipe(self):
        pp.pprint(super().__repr__())


class Room(PrittyPrinter):
    def __init__(self, room_details={}, in_use={}):
        self.room_details = room_details
        self.in_use = in_use
    
    def __getitem__(self, item):
        return self.room_details[item]
    
    def __setitem__(self, item, value):
        self.room_details[item] = value

    def __delitem__(self, item):
        del self.room_details[item]

    def __iter__(self):
        return iter(self.room_details)

    def __len__(self):
        return len(self.room_details)
    
    def __repr__(self):
        return self.room_details
    
    def __str__(self):
        return "Nr: {}. Type: {}\nFacilities: {}".format(self.room_details['nr'], self.room_details['type'], self.room_details['facilities'])

    def __add__(self, other):
        if self.room_details['type'] != other.room_details['type']:
            raise ValueError("Incompatible room types for sum")
        elif self.room_details['nr'] == other.room_details['nr']:
            raise ValueError("Incompatible room number for sum")
        elif self.room_details['floor'] != other.room_details['floor']:
            raise ValueError("Incompatible room floor for sum")
        lst = self.room_details['facilities']
        lst.extend(other.room_details['facilities'])
        return Room({'nr':self.room_details['nr'], 'type':self.room_details['type'], 'floor':self.room_details['floor'], 'facilities':list(set(lst))}, {})


class Room_Inventory():
    """a mutable sequence that holds rooms"""

    price = {'single_room': 100, 'double_room': 170}

    def __init__(self, rooms=[]):
        self.rooms = rooms
    
    def __getitem__(self, item):
        return self.rooms[item]
    
    def __setitem__(self, item, value):
        self.rooms[item] = value

    def __delitem__(self, item):
        del self.rooms[item]

    def __len__(self):
        return len(self.rooms)

    def __str__(self):
        result = ""
        for room in self.rooms:
            result += room.room_details['nr'] + " - " + room.room_details['type'] + "\n"
        return result
    
    def __repr__(self):
        return self.rooms

    def insert(self, item, value):
       self.rooms.insert(item, value)

    def append(self, item):
        self.rooms.append(item)
    
    def reserve(self, room_id, user_id, interval):
        for room in self.rooms:
            if room.room_details['nr'] == room_id:
                room.in_use.update({user_id:[interval[0], interval[1]]})
                return "Room {} reserved by {}".format(room.room_details['nr'], user_id)
        return "Room number not found"
    
    def check_availability(self, room_type, period):
        available_rooms = []
        for room in self.rooms:
            if room_type == room.room_details['type']:
                if len(room.in_use):
                    time_check = any([(interval[0] <= period[0] <= interval[1]) or (interval[0] <= period[1] <= interval[1]) for interval in room.in_use.values()])
                    if not time_check:
                        available_rooms.append(room.room_details['nr'])
                else:
                    available_rooms.append(room.room_details['nr'])
        return available_rooms


class Client(PrittyPrinter):
    """a mutable mapping that holds client details an their reserved rooms"""

    def __init__(self, user_id, client_details={}, reserved_room={}):
        self.user_id = user_id
        self.client_details = client_details
        self.reserved_room = reserved_room

    def __getitem__(self, item):
        return self.client_details[item]
    
    def __setitem__(self, item, value):
        self.client_details[item] = value

    def __delitem__(self, item):
        del self.client_details[item]

    def __len__(self):
        return len(self.client_details)

    def __iter__(self):
        return iter(self.client_details)
    
    def __repr__(self):
        return self.client_details

    def __str__(self):
        return "{} {} {}".format(self.client_details['name'], self.client_details['surname'], self.user_id)

    def __contains__(self, item):
        return item in self.client_details

    def update(self, item):
        self.client_details.update(item)

    def status(self):
        result = ""
        rooms_reserved = ""
        for key, value in self.client_details.items():
            result += "{}: {}\n".format(key, value)
        for key, value in self.reserved_room.items():
            rooms_reserved += "rooms reserved:\n Room nr:{}, for period: {} - {}\n".format(key, value[0], value[1])
        return "{0}\n{1}\n{0}\nid: {2}\n{3}\n{0}\n{4}".format("*"*16, "Client status", self.user_id, result, rooms_reserved)


class Clients():
    """a mutable sequence that holds our clients"""

    def __init__(self, clients_list=[]):
        self.clients_list = list(clients_list)

    def __getitem__(self, item):
        return self.clients_list[item]
    
    def __setitem__(self, item, value):
        self.clients_list[item] = value

    def __delitem__(self, item):
        del self.clients_list[item]

    def __len__(self):
        return len(self.clients_list)

    def __str__(self):
        result = "ID | Name | Surname"
        for client in self.clients_list:
            result += "{} | {} | {} \n".format(client.user_id, client.client_details['name'], client.client_details['surname'])
        return result
    
    def __repr__(self):
        return self.clients_list

    def insert(self, item, value):
        self.clients_list.insert(item, value)

    def append(self, client):
        self.clients_list.append(client)

    def check_client(self, name, surname):
        for client in self.clients_list:
            if client.client_details['name'] == name and client.client_details['surname'] == surname:
	            return client.user_id
            else:
                return 0
    
    def get_user(self, id):
        for client in self.clients_list:
            if client.user_id == id:
                return client.client_details['name'] + ' ' + client.client_details['surname']
        return None

    def new_client(self, name, surname, age, address):
        lst = []
        for client in self.clients_list:
            lst.append(client.user_id)
        id = choice(list(set(range(1, 1000)) - set(lst)))
        new_client = Client(id, {'name':name, 'surname':surname, 'age':age, 'address':address}, reserved_room={})
        self.clients_list.append(new_client)
        return new_client.user_id

    def reserve(self, room_id, user_id, interval):
        for client in self.clients_list:
            if client.user_id == user_id:
                client.reserved_room.update({room_id:[interval[0], interval[1]]})
                return "Client {} reserved the room nr: {}".format(client.user_id, room_id)
        return "Client not found in database"
