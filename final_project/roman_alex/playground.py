from application import *

new_client_1 = "John.Doe.USA.(001)2222-2222.HoneyWell"
new_client_2 = "Jane.Doe.Canada.(002)3333-3333.Regor"

# Creating and checking client_1 form a string
client_1 = Client.from_string(new_client_1)
print(vars(client_1))

# Creating and checking client_2 form a string
client_2 = Client.from_string(new_client_2)
print(vars(client_2))

# Creating and checking client_3 (standard)
client_3 = Client("Joe", "Smith", "USA", "(001)4444-4444", "HoneyWell")
print(vars(client_3))

# testing mixin method for the custom repr and str
client_1
print(client_1)

# testing full_name method
client_1.full_name()

# creating the client list
client_lists = [
    Client.from_string(new_client_1),
    Client.from_string(new_client_2)
]

client_list = Client_List(client_lists)

# testing add_client method
client_list.add_client(client_3)

# testing delete_client method
client_list.delete_client(client_3)

# creating new products & testing class method
new_product_1 = "Mouse.155.Wireless"
new_product_2 = "Keyboard.255.Wired"
new_product_3 = "Display.2550.LED"

product_1 = Product.from_string(new_product_1)
product_2 = Product.from_string(new_product_2)
product_3 = Product.from_string(new_product_3)

# testing operator overloading
product_1 + product_2

# creating new products & testing class method
new_product_4 = "Display.2550.LED.Requires support"
product_4 = Special_Product.from_string(new_product_4)

# testing inheritance
print(product_4.name)
print(product_4.special_notes)

# creating the inventory
shop_inventory = Inventory(product_1, 10)

# adding products to inventory
shop_inventory.add_product(product_2, 20)
shop_inventory.add_product(product_3, 30)

# updating a quantity
shop_inventory.update_inventory(product_3, 10)
print(shop_inventory)

# purchasing an item
purchase(client_1, product_2, shop_inventory)

# testing the loyalty update
purchase(client_1, product_3, shop_inventory)
purchase(client_1, product_3, shop_inventory)
purchase(client_1, product_3, shop_inventory)
print(client_1.loyalty)
