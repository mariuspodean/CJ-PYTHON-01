import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


# mixin method
class PrettyPrinterMixin:

    def __str__(self):
        dash = '*' * 20
        result = '{} \n{} \n{} \n '.format(dash, self.full_name(), dash)
        return result

    def __repr__(self):
        result = 'Name: {}'.format(self.full_name())
        return result


class Client(PrettyPrinterMixin):
    no_of_clients = 0

    def __init__(self, first_name, last_name, country, telephone, company):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.telephone = telephone
        self.company = company
        self.total_spent = 0
        self.purchases = []
        self.loyalty = "Basic"
        Client.no_of_clients += 1

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @classmethod
    def from_string(cls, client_str):
        first_name, last_name, country, telephone, company = client_str.split(".")
        return cls(first_name, last_name, country, telephone, company)

# mutable sequence
class Client_List:
    def __init__(self, iterable):
        self.client_list = list(iterable)

    def __iter__(self):
        return iter(self.client_list)

    def __len__(self):
        return len(self.client_list)

    def __getitem__(self, index):
        return self.client_list[index]

    def __setitem__(self, key, item):
        if key >= len(self):
            self.client_list.extend(key + 1)
        self.client_list[key] = item

    def __delitem__(self, key):
        del (self.client_list[key])

    def __str__(self):
        print_list = str('Current clients are: ')
        for client in self.client_list:
            print_list += '{}, '.format(client.full_name())
        return print_list

    def __repr__(self):
        print_list = ''
        for client in self.client_list:
            print_list += '{}, '.format(client.full_name())
        return print_list

    def add_client(self, client):
        self.client_list.append(client)
        return self.client_list

    def delete_client(self, client):
        self.client_list.remove(client)
        return self.client_list


class Product:

    def __init__(self, name, price, info):
        self.name = name
        self.price = int(price)
        self.info = info

    def __str__(self):
        result = '{}'.format(self.name)
        return result

    def __repr__(self):
        result = 'Name: {}'.format(self.name)
        return result

    # operator overloading and logging
    def __add__(self, other):
        name = self.name + ' & ' + other.name
        logging.debug(name)
        price = self.price + other.price
        logging.debug(price)
        info = self.info + ' & ' + other.info
        logging.debug(info)
        return Product(name, price, info)

    @classmethod
    def from_string(cls, client_str):
        name, price, info = client_str.split(".")
        return cls(name, price, info)


# inheritance
class Special_Product(Product):

    def __init__(self, name, price, info, special_notes):
        super().__init__(name, price, info)
        self.special_notes = special_notes

    def __str__(self):
        result = '{}'.format(self.name)
        return result

    def __repr__(self):
        result = 'Name: {}'.format(self.name)
        return result

    @classmethod
    def from_string(cls, client_str):
        name, price, info, special_notes = client_str.split(".")
        return cls(name, price, info, special_notes)


# mutable mapping
class Inventory:
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty
        self.inventory = {product: qty}

    def __iter__(self):
        return iter(self.inventory)

    def __len__(self):
        return len(self.inventory)

    def __getitem__(self, index):
        return self.inventory[index]

    def __setitem__(self, key, value):
        self.inventory[key] = value

    def __delitem__(self, key):
        del (self.inventory[key])

    def pop(self):
        return self.inventory.pop

    def keys(self):
        return self.inventory.keys()

    def values(self):
        return self.inventory.values()

    def __str__(self):
        print_list = str('Current available products are:\n')
        for index, item in enumerate(self.inventory, start=1):
            print_list += '{}:{} {} \n'.format(index, item, self.inventory[item])
        return print_list

    def add_product(self, product, qty):
        self.inventory.update({product: qty})
        return self.inventory

    def delete_product(self, product):
        self.inventory.pop(product)
        return self.inventory

    def update_inventory(self, product, qty):
        if int(qty) > 0:
            if product in self.inventory.keys():
                self.inventory[product] += qty
            else:
                print("('{} in not in the current inventory!'.format(name))")
        else:
            if product in self.inventory.keys():
                print(self.inventory[product])
                self.inventory[product] -= -qty
                if self.inventory[product] == 0:
                    self.inventory.pop(product)
                    return self.inventory
            else:
                print("('{} in not in the current inventory!'.format(name))")


def create_purchase_data(func):
    def wrapper(client, product, inventory):
        for key in inventory.keys():
            if str(key) == str(product.name):
                inventory.update_inventory(product, -1)
                if client.total_spent < 2000:
                    client.total_spent = client.total_spent + (product.price * 1)
                    logging.debug(client.total_spent)
                else:
                    if 2000 <= client.total_spent < 4000:
                        client.loyalty = "Silver"
                        logging.debug(client.loyalty)
                        client.total_spent = client.total_spent + (product.price * 0.9)
                        logging.debug(client.total_spent)
                    else:
                        if client.total_spent >= 4000:
                            client.loyalty = "Gold"
                            logging.debug(client.loyalty)
                            client.total_spent = client.total_spent + (product.price * 0.7)
                            logging.debug(client.total_spent)
    return wrapper


#decorator
@create_purchase_data
def purchase(client, product, inventory):
    separator = '-' * 50
    file = open("purchase_log", "a")
    file.write('Client Name: {}'.format(client.full_name()))
    file.write('\n')
    file.write('Purchased item: {}'.format(product.name))
    file.write('\n')
    file.write('{}'.format(separator))
    file.write('\n')
    file.close()
    purchase_info = [client, product, inventory]
    return purchase_info
