from application import *
import unittest


class Test_Client(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Starting Test")

    @classmethod
    def tearDownClass(cls):
        print("Ending Test")

    def setUp(self):
        print("Set_Up")
        self.test_client_1 = Client("John", "Doe", "USA", "(001)4444-4444", "HoneyWell")
        self.test_client_2 = Client("Jane", "Doe", "USA", "(001)3333-4444", "Regor")

    def client_class_test_full_name(self):
        print("Testing the full_name method from the Client class")
        self.assertEqual(self.test_client_1.full_name(), "John Doe")
        self.assertEqual(self.test_client_2.full_name(), "Jane Doe")

        self.test_client_1.first_name = "Carl"
        self.test_client_2.first_name = "Susan"

        self.assertEqual(self.test_client_1.full_name(), "Carl Doe")
        self.assertEqual(self.test_client_2.full_name(), "Susan Doe")

    def test_client_list_add_client(self):
        print("Testing the add_client method from the Client_List class")
        test_client_generator_list = [self.test_client_1]
        test_client_list = Client_List(test_client_generator_list)
        self.assertEqual(len(test_client_list), 1)
        print(test_client_list)

        test_client_list.add_client(self.test_client_2)
        print(test_client_list)
        self.assertEqual(len(test_client_list), 2)

    def test_client_list_delete_client(self):
        print("Testing the delete_client method from the Client_List class")
        test_client_generator_list = [self.test_client_1,self.test_client_2]
        test_client_list = Client_List(test_client_generator_list)
        self.assertEqual(len(test_client_list), 2)
        print(test_client_list)

        test_client_list.delete_client(self.test_client_2)
        print(test_client_list)
        self.assertEqual(len(test_client_list), 1)

if __name__ == '__main__':
    unittest.main()
