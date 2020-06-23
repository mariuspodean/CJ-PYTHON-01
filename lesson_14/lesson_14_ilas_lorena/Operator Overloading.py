"""
Create a Report (parent class) for two services (child classes). Each service has three attributes (if you can think of
more you are welcome to add them!)service_name, revenue and expenses.
- Create a mixin class to calculate the net revenue
- Use then all your information to calculate the total net revenue for the two services using operator overloading
- As a bonus you can also calculate the percentage of expenses also in the mixin class
"""


class Report:

    def __init__(self, service_name):
        self.service_name = service_name


class CalculationsMixin:

    def calculate_expenses_percentage(self):
        percentage = self.expenses * 100 // self.revenue
        return f'Expenses are {percentage}% of revenues'

    def calculate_net_revenue(self):
        return self.revenue - self.expenses


class Service1(Report, CalculationsMixin):

    def __init__(self, service_name, revenue, expenses):
        super().__init__(service_name)
        self.revenue = revenue
        self.expenses = expenses
        self.net_revenue = self.calculate_net_revenue()


class Service2(Report, CalculationsMixin):

    def __init__(self, service_name, revenue, expenses):
        super().__init__(service_name)
        self.revenue = revenue
        self.expenses = expenses
        self.net_revenue = self.calculate_net_revenue()

    def __add__(self, other):
        return f'Total Net Revenue for {self.service_name} and {other.service_name} is € ' \
               f'{self.net_revenue + other.net_revenue}'


service1 = Service1('E-Commerce websites', 10000, 3000)
service2 = Service2('Blog websites', 15000, 1000)

print(service1.calculate_expenses_percentage())
print(f'Net revenue for {service1.service_name} is € {service1.calculate_net_revenue()}')
print(service2 + service1)



