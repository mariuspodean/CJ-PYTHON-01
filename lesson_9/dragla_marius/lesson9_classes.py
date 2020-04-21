# Build two classes of your choice that can model a real-life example. The class needs to meet the following requirements:
#     at least 5 attributes each
#     at least 2 methods each
#     one class to inherit from another
# As a demonstration create at least 5 instances of one class (preferably the child class) and call all the methods it holds
# Ex: You can have one class (Country) that has general attributes about countries such as area, neighbours, cities etc and methods related to those attributes.
# The second class can be a specific country (Romania) that has more specific attributes such as attractions, universities etc.

class Products(object):

    def __init__(self, category, brand, model, stock, price):
        self.category = category
        self.brand = brand
        self.model = model
        self.stock = stock
        self.price = price

    def category_check(self):
        if self.category is 'Laptop':
            return 'Category: Computers'
        else:
            return 'Category: Others'

    def on_stock(self):
        if self.stock > 0:
            return 'Availability: On stock'
        else:
            return 'Availability: Out of stock'

    def price_euro(self):
        return int(f'{self.price}')*0.21


class Laptop(Products):

    def __init__(self, category, brand, model, stock, price, display, feature):
        self.display = display
        self.feature = feature
        super().__init__(category, brand, model, stock, price)

    def description(self):
        return f'{self.category} {self.brand} {self.model} {self.display}'

    def special_feature(self):
        if self.feature is None:
            return 'No special feature'
        else:
            return f'Special feature: {self.feature}'


lenovo = Laptop('Laptop', 'Lenovo', 'IdeaPad L340', 5, 5999, '17,3"', 'Touchscreen')
hp = Laptop('Laptop', 'HP', 'Pavilion', 2, 3999, '15,6"', '4K')
asus = Laptop('Laptop', 'Asus', '8565U', 4, 2999,'14"', None)
dell = Laptop('Laptop', 'Dell', 'Alienware', 0, 9999,'17"', 'Gaming')
apple = Laptop('Laptop', 'Apple', 'Macbook Air', 1, 5999,'13"', 'Ultraportable')

print(lenovo.description())
print(lenovo.special_feature())
print(lenovo.category_check())
print(lenovo.on_stock())
print(lenovo.price_euro())
print('-----')
print(dell.description())
print(dell.on_stock())
print('-----')
print(asus.description())
print(asus.special_feature())