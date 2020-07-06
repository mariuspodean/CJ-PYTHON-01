import unittest
from backend import PrittyPrinter, Room, Room_Inventory, Client, Clients
import datetime
import yaml

date1 = datetime.date.today()
date2 = date1 + datetime.timedelta(days=3)

class Test_Room(unittest.TestCase):

    def test_room_object_attribute_initialization(self):
        with open('rooms.yaml') as file:
            hotel_rooms = yaml.load(file)

        room = Room(hotel_rooms['room1'], {'1':[date1, date2]})

        self.assertEqual(room.room_details['type'], "single_room"), 'room instance did not load correctly'
        self.assertIsInstance(room, Room)


class Test_Room_Inventory(unittest.TestCase):

    def test_room_inventory_object_attribute_initialization(self):
        room1 = Room({'nr':2, 'type': "single_room", 'floor': 1, "facilities": "dishwasher"}, {'1':[date1, date2]})

        rooms = Room_Inventory([])
        rooms.append(room1)

        self.assertIsInstance(rooms, Room_Inventory)
        self.assertIsInstance(rooms.rooms, list)
        self.assertEqual(rooms.rooms[0].room_details['type'], "single_room")


class Test_Client(unittest.TestCase):

    def test_client_object_attribute_initialization(self):
        client1 = Client(1, {'name':'Test', 'surname':'Surtest', 'age':'1', 'address':'Tests 1'}, {})

        self.assertEqual(client1.client_details['age'], "1"), 'client instance did not load correctly'
        self.assertIsInstance(client1, Client)


class Test_Clients(unittest.TestCase):

    def test_clients_inventory_object_attribute_initialization(self):
        client2 = Client(100, {'name':'Test2', 'surname':'Surtest2', 'age':'2', 'address':'Tests 2'}, {})

        clients = Clients([])
        clients.append(client2)

        self.assertIsInstance(clients, Clients)
        self.assertIsInstance(clients.clients_list, list)
        self.assertEqual(clients.clients_list[0].client_details['name'], "Test2")


if __name__ == '__main__':
    unittest.main()