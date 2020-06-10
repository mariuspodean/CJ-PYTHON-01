# Build two classes of your choice that can model a real-life example. The class needs to meet the following
# requirements:

# at least 5 attributes each
# at least 2 methods each
# one class to inherit from another

# As a demonstration create at least 5 instances of one class (preferably the child class) and call all the methods
# it holds

class Client:
    no_of_clients = 0

    def __init__(self, first_name, last_name, country, telephone, company):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.telephone = telephone
        self.company = company
        Client.no_of_clients += 1

    def full_name(self):
        return '{}{}'.format(self.first_name, self.last_name)

    @classmethod
    def from_string(cls, client_str):
        first_name, last_name, country, telephone, company = client_str.split(".")
        return cls(first_name, last_name, country, telephone, company)


new_client_1 = "John.Doe.USA.(001)2222-2222.HoneyWell"
new_client_2 = "Jane.Doe.Canada.(002)3333-3333.Resor"

# Creating and checking client_1 form a string
client_1 = Client.from_string(new_client_1)
print(client_1.__dict__)

# Creating and checking client_2 form a string
client_2 = Client.from_string(new_client_2)
print(client_2.__dict__)

# Creating and checking client_3
client_3 = Client("Joe", "Smith", "USA", "(001)4444-4444", "HoneyWell")
print(client_3.__dict__)


class Gold_Client(Client):
    def __init__(self, first_name, last_name, country, telephone, company, discount):
        self.discount = discount
        super().__init__(self, first_name, last_name, country, telephone, company)

    def gold_client_discount(self):
        return '{} %'.format(self.discount)

    def increase(self):
        if int(self.discount) <= 60:
            self.discount = int(self.discount) + 10
            return self.discount
        else:
            return print("Discount is already at maximum")


client_5 = Gold_Client("Jake", "fisher", "USA", "(001)4444-4444", "J.Walker", "20")
print(client_5.gold_client_discount())
client_5.increase()

import unitest
