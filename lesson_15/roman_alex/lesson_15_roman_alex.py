from lesson_9_roman_alex.py import Client, Gold_client
import unittest


class Test_Gold_Client(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Starting Test")

    @classmethod
    def tearDownClass(cls):
        print("Ending Test")

    def setUp(self):
        self.new_client_1 = Gold_Client("John", "Doe", "USA", "(001)4444-4444", "HoneyWell", "20")
        self.new_client_2 = Gold_Client("Jane", "Doe", "USA", "(001)3333-4444", "Regor", "30")

    def test_fullname(self):
        self.assertEqual(self.new_client_1.fullname, "John Doe")
        self.assertEqual(self.new_client_2.fullname, "Jane Doe")

        new_client_1.first_name = "Carl"
        new_client_2.first_name = "Susan"

        self.assertEqual(new_client_1.fullname, "Carl Doe")
        self.assertEqual(new_client_2.fullname, "Susan Doe")

    def test_increase(self):
        new_client_1.increase()
        new_client_2.increase()

        self.assertEqual(new_client_1.discount, 30)
        self.assertEqual(new_client_2.discount, 40)