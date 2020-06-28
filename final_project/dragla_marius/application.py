import csv
from collections.abc import MutableMapping, Sequence
import logging
import matplotlib.pyplot as plt
from faker import Faker

# Logging
logger = logging.getLogger(__name__)
module_name = '<< {} >> '.format(__name__)
logging.basicConfig(level=logging.INFO)


def get_customer_category_sales(csv_file):
    customer_category_sales = {}
    with open(csv_file) as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)
        for cust_name, _, _, _, categ, _, sales in csv_reader:
            if cust_name not in customer_category_sales.keys():
                category_sales = {categ: round(float(sales), 2)}
                customer_category_sales[cust_name] = category_sales
            else:
                if categ not in category_sales:
                    category_sales[categ] = round(float(sales), 2)
                else:
                    category_sales[categ] += round(float(sales), 2)
        return customer_category_sales


def instantiate_class(customers_category_sales, id_generator, sales):
    for customer_name in customers_category_sales.keys():
        customer_id = next(id_generator)
        fake = Faker()
        customer_total_sales = sum(customers_category_sales[customer_name].values())
        customer_account = CustomerAccount(customer_name, customer_id, fake.address(), customers_category_sales[customer_name], customer_total_sales)
        sales.add_customer(customer_account)


# Generator
def generate_customer_id():
    customer_id = 1
    while True:
        yield f'Id{customer_id}'
        customer_id += 1


# Operators overloading
class CustomerAccount:

    def __init__(self, name, customer_id, address, category_sales, total_sales):
        self.name = name
        self.customer_id = customer_id
        self.address = address
        self.category_sales = category_sales
        self.total_sales = round(total_sales, 2)

    def __str__(self):
        dash = '*' * len(f'Name: {self.name}')
        display = str(f'{dash} \nName: {self.name} \n{dash}'
                      f'\nCustomer ID: {self.customer_id} \nAddress: {self.address}'
                      f'\nTotal Sales: {self.total_sales} \n')
        return display

    def __add__(self, other):
        customer_account1 = sum(self.category_sales.values())
        customer_account2 = sum(other.category_sales.values())
        return customer_account1 + customer_account2

    def __radd__(self, other):
        return sum(self.category_sales.values()) + other

    def __getitem__(self, index):
        return self.customer_id[index]


# Sequence collection with custom str and repr methods
class AllCategorySales(Sequence):

    def __init__(self, category_sales):
        self.category_sales = category_sales

    @staticmethod
    def get_total_category_sales(customers_category_sales):
        category_sales = {}
        for categ_sales in customers_category_sales.values():
            for categ, sales in categ_sales.items():
                if categ in category_sales:
                    category_sales[categ] += round(sales, 2)
                else:
                    category_sales[categ] = round(sales, 2)
        return category_sales

    @staticmethod
    def get_category_sales_perc(category_sales, total_sales):
        sales_percentages = {}
        for categ, sales in category_sales.items():
            if categ not in sales_percentages:
                sales_percentages[categ] = round((sales / total_sales * 100), 2)
        return sales_percentages

    def __str__(self):
        display = [f'Category Sales\n']
        for category, sales in self.category_sales.items():
            display.append(f'{category}: {sales}')
        return '\n'.join(display)

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}'

    def __getitem__(self, category):
        return self.category_sales[category]

    def __len__(self):
        return len(self.category_sales)


# MutableMapping collection with custom str and repr methods, Inheritance
class Sales(AllCategorySales, MutableMapping):

    def __init__(self, all_categories_sales):
        self.customers = []
        super().__init__(all_categories_sales)

    def add_customer(self, customer):
        return self.customers.append(customer)

    def __str__(self):
        main_menu_selection = int(input())
        if main_menu_selection == 1:
            logger.info("input1")
            dash = '*' * len('Customer Accounts')
            display_customers = [f'{dash}\nCUSTOMER ACCOUNTS\n{dash}\nNumber of accounts: {len(self.customers)}\n']
            for cust in self.customers:
                display_customers.append(f'{cust.customer_id}: {cust.name}')
            return ' | '.join(display_customers)
        else:
            if main_menu_selection == 2:
                logger.info("input2")
                display_categories = [f'Category Sales\n']
                for category, sales in self.category_sales.items():
                    display_categories.append(f'{category}: {round(sales, 2)}')
                return '\n'.join(display_categories)


    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}'

    def search_customer(self, input_value):
        for customer in self.customers:
            if input_value.casefold() == customer.name.casefold() \
                    or input_value.casefold() == customer.customer_id.casefold():
                return customer
        else:
            return 'Customer not found'

    def __getitem__(self, index):
        return self.customers[index]

    def __delitem__(self, key):
        del self.customers[key]

    def __setitem__(self, key, value):
        self.customers[key] = value

    def __iter__(self):
        return iter(self.customers)

    def __len__(self):
        return len(self.customers)

    def get_total_sales(self):
        return sum(self.customers)


# Context Manager with logging
class ReportGenerator:

    def __init__(self, report_type, sales):
        self.report_type = report_type
        self.sales = sales

    def __enter__(self):
        logger.info('Entering Context Manager, opening file')
        if self.report_type == 1:
            print("Please insert customer name or ID:")
            input_customer = input()
            self.file = open('Customer_category_report.csv', mode='w')

            customer = self.sales.search_customer(input_customer)
            sales_per_category = customer.category_sales

            self.file.write(f'Customer Category Sales Report \n\n')
            self.file.write(f'Sales per category: {sales_per_category}')

            self.file.close()
            logger.info('Report has been generated')
            self.file = open('Customer_category_report.csv', mode='r')

        else:
            if self.report_type == 2:
                self.file = open("Total_Report.csv", mode='w')

                total_sales = self.sales.get_total_sales()
                total_customers = len(self.sales)
                category_sales = self.sales.category_sales
                sales_percentages = AllCategorySales.get_category_sales_perc(category_sales, total_sales)

                labels = sales_percentages.keys()
                sizes = sales_percentages.values()
                explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)

                plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)

                plt.axis('equal')
                plt.show()

                self.file.write(f'Totals Report \n\n')
                self.file.write(f'Total accounts: {total_customers} \nTotal sales: {round(total_sales, 2)} '
                                f'\nTotal sales per category: \n{category_sales}')

                self.file.close()
                logger.info('Report has been generated')
                self.file = open("Total_Report.csv", mode='r')

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info('Exiting Context Manager, closing file')
        self.file.close()

