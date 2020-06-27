import random
import csv
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# nice display
class PrittyPrinterMixin:

    def display(self):
        return ["{0}. {1}: {2}".format(index + 1, key, value)
                for index, (key, value) in enumerate(self.contents())]

    def order_display(self):
        separator = "*" * 25
        return "\n".join([
            separator, 'Data comanda: ', self.order_date, 'Client: ', self.client, 'Adresa: ', self.address,
            separator + "\n",
            *self.display(), "\n", separator, "\n"
        ])

    def stock_display(self):
        separator = "*" * 25
        return "\n".join([
            separator, 'Stocks: ', separator + "\n", *self.display(), "\n", separator, "\n"
        ])


'''Order class holds the orders from the clients
has order_date, client, address and order_details (dictionary)'''


class Order(PrittyPrinterMixin):

    def __init__(self, order_date, client, address, order_details):
        self.order_date = order_date
        self.client = client
        self.address = address
        self.order_details = order_details

    def contents(self):
        return self.order_details.items()

    def __str__(self):
        return self.order_display()

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.order_date,
            self.client, self.order_details, id(self)
        )

    def __iter__(self):
        return iter(self.order_details)

    def __getitem__(self, item):
        return self.order_details[item]

    def __len__(self):
        return len(self.order_details)

    def keys(self):
        return self.order_details.keys()

    def __eq__(self, other):
        return self.client == other

    def client(self):
        return self.client

    '''order_add_from_csv() method is for extracting
        class Order attributes from a CSV file'''

    def order_add_from_csv(*args):
        logger.debug("\n Add order from CSV file \n")
        with open('comanda.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                if len(line[0]) > 0:
                    order_date = line[0]
                    client = line[1]
                    address = line[2]
                    order_details = {line[3]: line[4]}
                else:
                    order_details.update({line[3]: line[4]})
            client_order_date = Order(order_date, client, address, order_details)
            return client_order_date


'''Stock class is for keeping the inks that are present in delivery from point
with code and quantity'''


class Stock(PrittyPrinterMixin):

    def __init__(self):
        self.client = "Stock"
        self.inks = {}

    def contents(self):
        return self.inks.items()

    def __str__(self):
        return self.stock_display()

    def __repr__(self):
        return str(self.stock_display())

    def __setitem__(self, key, value):
        if value:
            self.inks[key] = value
            return
        print('Ink  {} will be removed completely from the Stock!\n'
              .format(key))
        del self.inks[key]

    def __delitem__(self, key):
        del self.inks[key]

    def __iter__(self):
        return self.inks

    def __len__(self):
        return len(self.inks)

    def __contains__(self, key):
        return key in self.inks.keys()

    def append(self, ink, quantity):
        logger.debug("\n Append method to Stock class ---adding ink code/quantity  to Stocks")
        self.inks[ink] = quantity
        if not ink or not quantity:
            pass

    def check_order(self, order):
        available, not_available = [], []
        for item in order.keys():
            product = available if item in self else not_available
            product.append(item)

        return available, not_available

    def check_is_enough_quantity(self, item, value):
        if item not in self:
            return 0
        if value > self.inks[item]:
            return value - self.inks[item]
        return None

    ''' Adds ink code/quantity to Stock instance from
    a CSV file using DictReader
        Counting time that is needed for this operation
    and displaying using loggin  '''

    def add_from_csv(self):
        logger.info('\nAdd inks in stock from CSV file\n')
        start = time.time()
        with open('in_stock.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            print('Code and quantity inks from CSV file:\n')
            for line in csv_reader:
                print('Ink code: {} Quantity: {}'.format(line['ink'], line['quantity']))
                if line['ink'] not in self.inks.keys():
                    self.append(line['ink'], line['quantity'])
                else:
                    a = (line['ink'])
                    b = (line['quantity'])
                    self.inks[a] += int(b)
        end = time.time()
        logger.info('\nQuerying took {}s\n'.format(end - start))


def check_the_stock(stock, orders_box):
    return [(order.client, order.order_date) for order in orders_box.contents()
            if len(stock.check_order(order)[1]) < 1]


def archive_unavailable_inks_list(func):
    def wrapper(stock, order):
        unavailable_inks_list_archive.append(func(stock, order))

    return wrapper


def pretty_print_order(func):
    def wrapper(stock, order):
        unavailable_inks_list = func(stock, order).items()
        list_str = "\n".join(["\t| {0}. {1}: {2} {3}|.".format(
            index + 1, key, value, (22 - (len(str(index + 1)) + len(str(key)) + len(str(value)))) * " ")
            for index, (key, value) in enumerate(unavailable_inks_list)])
        print("".join([
            __header__,
            "\t| Unavailable inks list:     |. \n",
            "\t| \t\t\t\t\t\t\t |.\n",
            "\t| \t\t\t\t\t\t\t |.\n",
            list_str,
            __footer__
        ]))
        return func(stock, order)

    return wrapper


@archive_unavailable_inks_list
@pretty_print_order
def prepare_shipping_list(stock, order):
    unavailable_inks_list = {}
    for item, value in order.contents():
        stock_check = stock.check_is_enough_quantity(item, value)
        if stock_check is not None:
            unavailable_inks_list.update({item: value})
        else:
            pass

    return unavailable_inks_list


unavailable_inks_list_archive = []


# orders are kept in instance of Orderbox class
class OrderBox:

    def __init__(self):
        self.orders = []

    def contents(self):
        return self.orders

    def __iter__(self):
        return iter(self.orders)

    def __delitem__(self, key):
        del self.orders[key]

    def __getitem__(self, item):
        return self.orders[item]

    def __len__(self):
        return len(self.orders)

    def __str__(self):
        return str([(order.client, order.order_date, order.order_details) for order in self.orders])

    def append(self, order):
        return self.orders.append(order)

    def delete(self, order):
        self.orders.remove(order)

    def pick(self, client=None):
        if not client:
            return self.orders[random.randint(0, len(self) - 1)]
        elif client not in self.orders:
            return NameError(f'Recipe with the {client} does not exist.')

        for order in self.orders:
            if client == order.client:
                return order

    '''Selecting the orders that have inks in stock, based on 'insert_date',witch
    will return a list of orders
    Starting from the list above will make another list that
    will be the delivery order points'''


def shipping_order(in_stock_orders):
    insert_date = input("Please enter date in format yyyy-mm-dd")
    list_shipping_order = list()
    for i in range(len(in_stock_orders)):
        if in_stock_orders[i][1] == insert_date:
            list_shipping_order.append(in_stock_orders[i][0])
    print(list_shipping_order)
    new_list_shipping_order = list()
    for index in range(len(list_shipping_order)):
        option = input("Please select {} delivery point".format(index + 1))
        while option not in list_shipping_order or option in new_list_shipping_order:
            print('Input not in list of above or Already in delivery point list , please insert another')
            option = input("Please select {} delivery point".format(index + 1))
        new_list_shipping_order.append(option)

    print("\n Below is the list of orders received in {} : {}".format(insert_date, new_list_shipping_order))


__header__ = '''
   ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |                            |.
'''
__footer__ = r'''
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/__________________________/.
'''
