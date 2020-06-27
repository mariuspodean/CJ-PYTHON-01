from final_project_mihai_farcas.application import Order, Stock, OrderBox, shipping_order
from final_project_mihai_farcas.application import check_the_stock, prepare_shipping_list, unavailable_inks_list_archive

# Order
print("\n Create new orders: \n")

popescu_2020_06_09 = Order(
    "2020-06-09", "Popescu", "Moldoveanu str nr.6",
    {
        'HP 3002 BLK': 1,
        'HP 3002 YLL': 4,
        'HP 3002 CYA': 2,
        'HP 3002 MAG': 1,
    }
)
print(popescu_2020_06_09)
popescu_2020_06_09_order_details = list(popescu_2020_06_09.keys())

print(popescu_2020_06_09_order_details)

georgescu_2020_06_09 = Order(
    "2020-06-09", "Georgescu", "Vladesei nr.4",
    {
        'CANON 2051 BLK': 7,
        'HP 3002 BLK': 2,
        'KONICA 9000 MAG': 1
    }
)
print(georgescu_2020_06_09)
georgescu_2020_06_09_order_details = list(georgescu_2020_06_09.keys())
print(georgescu_2020_06_09_order_details)

paunescu_2020_06_09 = Order(
    "2020-06-09", "Paunescu", "Vladesei nr.4",
    {
        'KONICA 9000 CYA': 1,
        'HP 3002 YLL': 2,
        'KONICA 9000 MAG': 3
    }
)

print(paunescu_2020_06_09)
paunescu_2020_06_09_order_details = list(paunescu_2020_06_09.keys())
print(paunescu_2020_06_09_order_details)

cosma_2020_02_10 = Order(
    "2020-02-10", "Cosma", "Trandafirilor nr.1",
    {
        'HP 2500 BLK': 1,
        'HP 2500 MAG': 1,
        'HP 2500 CYA': 1,
        'HP 2500 YLL': 1,
        'HP 3002 YLL': 2,
        'KONICA 9000 MAG': 2
    }
)

print(cosma_2020_02_10)
cosma_2020_02_10_order_details = list(cosma_2020_02_10.keys())
print(cosma_2020_02_10_order_details)

cosma_2020_05_05 = Order(
    "2020-05-05", "Cosma", "Trandafirilor nr.1",
    {
        'HP 3002 MAG': 1,
        'HP 3002 YLL': 1,
    }
)

print(cosma_2020_05_05)
cosma_2020_05_05_order_details = list(cosma_2020_05_05.keys())

print(cosma_2020_05_05_order_details)

turdean_2020_05_05 = Order(
    "2020-05-05", "Turdean", "Vulcan nr.34",
    {
        'KONICA 9000 MAG': 1,
        'KONICA 9000 YLL': 1,
        'KONICA 9000 CYA': 1,
        'HP 2500 BLK': 2,
        'HP 2500 YLL': 2,
    }
)
print(turdean_2020_05_05)
turdean_2020_05_05_order_details = list(turdean_2020_05_05.keys())
print(turdean_2020_05_05_order_details)

muresan_2020_05_05 = Order(
    "2020-05-05", "Muresan", "Merilor nr.8",
    {
        'KONICA 9000 MAG': 1,
        'HP 2500 MAG': 5,
        'HP 2500 YLL': 2,
    }
)
print(turdean_2020_05_05)
turdean_2020_05_05_order_details = list(turdean_2020_05_05.keys())
print(turdean_2020_05_05_order_details)

# OrderBox
orders = OrderBox()

orders.append(popescu_2020_06_09)
orders.append(cosma_2020_05_05)
orders.append(turdean_2020_05_05)
orders.append(georgescu_2020_06_09)
orders.append(paunescu_2020_06_09)
orders.append(cosma_2020_02_10)
orders.append(muresan_2020_05_05)

print("\n Print Order Box:")
print(orders)

print('\nADD order from CSV\n')
orders.append(Order.order_add_from_csv())
print(orders)

# Stock
stock = Stock()

stock.append('CANON 2051 BLK', 7)
stock.append('HP 2500 YLL', 10)
stock.append('HP 2500 CYA', 10)
stock.append('HP 2500 MAG', 10)
stock.append('HP 3002 BLK', 20)
stock.append('HP 3002 YLL', 20)
stock.append('HP 3002 CYA', 20)
stock.append('HP 3002 MAG', 20)
stock.append('KONICA 9000 MAG', 10)
stock.append('KONICA 9000 YLL', 10)
stock.append('KONICA 9000 CYA', 10)
stock.append('KONICA 9000 BLK', 10)

print('initial \n {}'.format(stock))
# print('before importing from CSV file: \n {}'.format(stock))
stock.add_from_csv()
print("{} after importing from CSV file ".format(stock))

print("\n Delete ink code 'KONICA 9000 BLK' from the stock : \n")
del stock['KONICA 9000 BLK']
print(stock)

print("\n Prepare shipping for 'turdean_2020_05_05' order :\n")
unavailable_inks_list = prepare_shipping_list(stock, turdean_2020_05_05)
print('\nUnavailable ink list: {0}'.format(unavailable_inks_list_archive))

in_stock, not_in_stock = stock.check_order(turdean_2020_05_05)
print(turdean_2020_05_05)
print('\nAvailable inks: {0}'.format(in_stock))
print('Not available inks: {0}'.format(not_in_stock))

print("\n Check If inks from order are in Stock: \n")
in_stock_orders = check_the_stock(stock, orders)
print('Stock has inks for orders: {0}'.format(in_stock_orders))

shipping_order(in_stock_orders)
