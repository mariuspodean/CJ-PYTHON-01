from contextlib import contextmanager
import requests
import logging


class LoggerMixin(object):
    @property
    def logger(self):
        name = '.'.join([
            self.__module__,
            self.__class__.__name__
        ])
        return logging.getLogger(name)


class User(LoggerMixin):

    def __init__(self, name, password, user_type):
        self.name = name
        self.password = password
        self.user_type = user_type
        self.credentials = {}

    def __str__(self):
        return ("".join([
            __header__,
            "\t\t   |""   | Welcome back %s!" % self.name, "\t\t\t\t\t |\t  |",
            "\n\t\t   |""   | You are logged in as a %s!" % self.user_type, "\t\t\t |\t  |",
            __footer__
        ]))

    def __repr__(self):
        return f'{self.name} is a type {self.user_type}'


class Customer(User):

    def __init__(self, name, password):
        super().__init__(name, password, "Client")


class Driver(User):

    def __init__(self, name, password):
        super().__init__(name, password, "Driver")


__header__ = r'''

             ________________________________________________     
           /                                                  \          
           |    _________________________________________     |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
'''
__footer__ = r'''
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
'''

users = []
selected_option = None


@contextmanager
def open_file(name):
    f = open(name, 'r')
    try:
        yield f
    finally:
        f.close()


class Login(LoggerMixin):
    def __init__(self):
        self.credentials = {}
        self.current_user = None
        self.username = None

    def get_current_user(self):
        return self.current_user

    def __str__(self):
        return f'Login for {self.username}'

    def __repr__(self):
        return f'User {self.credentials}'

    def check(self, username, password):
        self.credentials[username] = password
        self.username = username

        with open_file('users.txt') as f:
            users_lines = f.read().splitlines()
            for user in users_lines:
                user_data = user.split(', ')
                temp_user = User(user_data[0], user_data[1], user_data[2])
                users.append(temp_user)

        user_exists = any(user.name == username and user.password == password for user in users)
        if user_exists:

            for user in users:
                if user.name == username:
                    self.current_user = user
            print(self.current_user)
        else:
            self.logger.error('Wrong Username or Password')

        return user_exists


class Parcel(LoggerMixin):

    def __init__(self, length, height, weight, address):
        self.length = length
        self.height = height
        self.weight = weight
        self.address = address
        self.reject = False
        self.dimensions = length * height

    def __str__(self):
        return f'Your Parcel has the following dimensions {self.length} x {self.height} and weights {self.weight}'

    def __repr__(self):
        return f'Parcel inputs {self.dimensions}'

    def __add__(self, other):
        return self.price() + other.price()

    def can_pay_cash(func):
        def inner(*args):
            ret = func(*args)
            if selected_option == "A":
                if args[0].weight <= 5:
                    print("You can pay cash for this parcel")
                else:
                    print("You cannot pay cash for this parcel")
            return ret

        return inner

    @can_pay_cash
    def price(self):
        """Find parcel's price."""
        if self.weight <= 5:
            return 10
        else:
            return 5 + self.weight

    def check(self):
        """Check the parcel's dimensions and weight."""
        self.reject = False

        if self.length > 50:
            print("Parcel too long.")
            self.reject = True

        if self.height > 50:
            print("Parcel too high.")
            self.reject = True

        if self.dimensions > 200:
            print("Parcel too large.")
            self.reject = True

        if self.weight < 1:
            print("Parcel too light.")
            self.reject = True

        if self.weight > 10:
            print("Parcel too heavy.")
            self.reject = True

        if self.reject:
            self.logger.error("Parcel rejected.")
        else:
            self.logger.info("Parcel accepted.")

        return self.reject


def inp_parcel():
    """Ask the user to input a parcel's data."""
    while True:
        try:
            inp_length = float(input("Enter the parcel's length: "))
            inp_height = float(input("Enter the parcel's height: "))
            inp_weight = float(input("Enter the parcel's weight: "))
            inp_address = input("Enter the delivery address: ")
            break
        except ValueError:
            print("\nERROR: Please enter proper numbers, e.g.: '45.55'.")
            print()

    parcel = Parcel(inp_length, inp_height, inp_weight, inp_address)
    print(parcel)
    return parcel


def customer_menu():
    """Display a menu for the user to select an option."""
    print("\nSelect an option:")
    print("\n\tA. Check a single parcel")
    print("\tB. Check multiple parcels")
    print("\tX. Exit")
    global selected_option
    selected_option = input("\nEnter your option: ").upper()
    if selected_option == "A":
        print()
        option_a()
    elif selected_option == "B":
        option_b()
    elif selected_option == "X":
        exit()
    else:
        print("\nERROR: Please enter a proper option, e.g.: 'A'.")
    customer_menu()


def option_a():
    """Single Parcel"""
    new_parcel = inp_parcel()
    print()
    new_parcel.check()

    if not new_parcel.reject:
        print("The delivery of this parcel will cost: ", new_parcel.price(), "\nThe delivery address is: ",
              new_parcel.address)
    print("*" * 50)


def option_b():
    """Batch of parcels"""
    batch_of_parcels = []
    total_price = 0
    while True:
        try:
            num_parcels = int(input("\nEnter the number of parcels: "))
            break
        except ValueError:
            print("\nERROR: Please enter an integer, e.g.: '5'.")
    for i in range(num_parcels):
        print("\nEnter parcel #%s's information:" % (i + 1))
        batch_of_parcels.append(inp_parcel())
        batch_of_parcels[i].check()

    for current_parcel, next_parcel in zip(batch_of_parcels, batch_of_parcels[1:]):
        total_price += current_parcel + next_parcel

    print()
    print("*" * 50)
    print("\nTotal price of delivery:", total_price)
    print("*" * 50)


# ===================================
# Driver section

class ConvertAddress:

    def __init__(self):
        self.addresses = []

    def __len__(self):
        return len(self.addresses)

    def __str__(self):
        return str([address for address in self.addresses])

    def __repr__(self):
        return f'The number of addresses are {len(self.addresses)}'

    def __getitem__(self, index):
        return self.addresses[index]

    def append(self, address):
        return self.addresses.append(address)


class AddressManager:

    @staticmethod
    def calculate_distance(current_point, next_point):
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + str(current_point[0]) + ',' + str(
            current_point[1]) + '&destinations=' + str(next_point[0]) + ',' + str(
            next_point[1]) + '&key=CUSTOM_API_KEY_NEEDED_HERE'
        response = requests.get(url).json()
        distance = response["rows"][0]["elements"][0]["distance"]["value"] / 1000  # distance in kms

        return distance

    @staticmethod
    def price_increase_generator(distances):
        increase_coeficient = 3
        generator = (distance * increase_coeficient for distance in distances)

        total_amount = 0
        for each in generator:
            total_amount += each

        return total_amount
