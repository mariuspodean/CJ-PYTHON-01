import os
from pprint import pprint

from final_project.mosut_sorin.main_data import *


def clear_screen():
    os.system("clear")


def enter_to_continue():
    input('\n\33[31mPress Enter to continue...\033[0m')


def check_value(value, d_b):
    try:
        if d_b.contains_check(value):
            return True
    except Exception as mesage:
        print(mesage)
        enter_to_continue()
        clear_screen()


def get_values_for_new_order_offer(cars_d_b, clients_d_b, operations_d_b):
    car_vin = input('Enter vehicle identification number (17 digits lenght): ')
    if not check_value(car_vin, cars_d_b):
        return None, None, None
    client_id = input('Enter client identification number: ')
    if not check_value(client_id, clients_d_b):
        return None, None, None
    order_operations_list = []
    question = 'Y'
    while question in ('Y', 'y'):
        operation = input('Enter operation: ')
        if not check_value(operation, operations_d_b):
            return None, None, None
        order_operations_list.append(operation)
        question = input('Do you want to add another operation [Y/N] :')
    return car_vin, client_id, order_operations_list


def new_order_offer(data_base_file, class_instance, vin, cl_id, ord_op_list):
    data_base = open_orders_file(data_base_file, OrdersArchive, class_instance)
    car_vin = vin
    client_id = cl_id
    order_operations_list = ord_op_list
    order_offer = open_new_order_offer(class_instance, car_vin, client_id, order_operations_list, data_base)
    save_order_offer(order_offer, data_base)
    # write_in_file(data_base_file, data_base)
    return order_offer


def close_order_offer(data_base_file, class_instance, order_number):
    data_base = open_orders_file(data_base_file, OrdersArchive, class_instance)
    order_offer = data_base[order_number]
    order_offer.close()
    # save_order_offer(order_offer, data_base)
    write_in_file(data_base_file, data_base)
    return data_base[order_number]


def add_two_orders(data_base_file, class_instance, first_o_no, second_o_no):
    data_base = open_orders_file(data_base_file, OrdersArchive, class_instance)
    sum_order = data_base[first_o_no] + data_base[second_o_no]
    save_order_offer(sum_order, data_base)
    write_in_file(data_base_file, data_base)
    return sum_order


def add_del_operations(data_base_file, class_instance, order_no, flag):
    data_base = open_orders_file(data_base_file, OrdersArchive, class_instance)
    order_to_update = data_base[order_no]
    print(f'Order to update:\n{order_to_update}')
    operations_to_add = []
    question = 'Y'
    while question in ('Y', 'y'):
        operation = input(f'Enter operation to {flag}: ')
        operations_to_add.append(operation)
        question = input(f'Do you want to {flag} another operation [Y/N] :')
    updated_order = add_delete_operation(order_to_update, operations_to_add, flag)
    save_order_offer(updated_order, data_base)
    write_in_file(data_base_file, data_base)
    return updated_order


def add_delete_just_parts(data_base_file, class_instance, order_no):
    data_base = open_orders_file(data_base_file, OrdersArchive, class_instance)
    order_to_update = data_base[order_no]
    print(f'Order to update:\n{order_to_update}')
    just_parts_dict = {}
    question = 'Y'
    while question in ('Y', 'y'):
        part_code = input(f'Enter the part code to add/delete: ')
        part_pieces = int(input(f'Enter how many pieces to add/delete (for delete use negative numbers): '))
        just_parts_dict.update({part_code: part_pieces})
        question = input(f'Do you want to add/delete another part? [Y/N] :')
    updated_order = add_just_parts(order_to_update, just_parts_dict, parts)
    save_order_offer(updated_order, data_base)
    write_in_file(data_base_file, data_base)
    return updated_order


def get_values_for_filters(cars_d_b=None, clients_d_b=None):
    car_vin = None
    client_id = None
    if cars_d_b:
        car_vin = input('Enter vehicle identification number (17 digits lenght): ')
        if not check_value(car_vin, cars_d_b):
            car_vin = None
    if clients_d_b:
        client_id = input('Enter client identification number: ')
        if not check_value(client_id, clients_d_b):
            client_id = None
    return car_vin, client_id


def check_number(number, d_b):
    try:
        if number in d_b:
            return True
    except Exception as mesage:
        print(mesage)
        enter_to_continue()
        clear_screen()


menu_dict = {
    'm1': 'MAIN MENU\n1.Orders/Offers\n2.Cars\n3.Clients\n4.Operations\n5.Spare Parts\n6.Exit',
    'm11': 'ORDERS/OFFERS MENU\n1.Open new order\n2.Open new offer\n3.Check order\n4.Check offer\n'
           '5.Add two orders\n6.Print orders/offers by car vin and status\n'
           '7.Print orders/offers by client id and status\n8.Print orders/offers betwin two dates and id and status\n'
           '9.Back',
    'm113': 'ORDER MENU\n1.Add operations in order\n2.Delete operations from order\n3.Add/Delete just parts\n'
            '4.Close order\n5.Back',
    'm114': 'OFFER MENU\n1.Add operations in offer\n2.Delete operations from offer\n3.Add/Delete just parts\n'
            '4.Close offer\n5.Back',
    'm12': 'CARS MENU\n1. Add new car\n2.Print car by vin\n3.Search car by registration number\n'
           '4.Print all cars\n5.Back',
    'm13': 'CLIENTS MENU\n1. Add new client\n2.Print client by client id\n3.Search client by name\n'
           '4.Print all clients\n5.Back',
    'm14': 'OPERATIONS MENU\n1.Add new operation\n2.Search operation by keyword\n3.Print all operations\n4.Back',
    'm15': 'SPARE PARTS MENU\n1.Search spare parts by part code\n2.Search spare parts by keyword\n'
           '3.Print all spare parts\n4.Back'

}

clear_screen()
print('HY, WELLCOME TO AUTO-SHOP-MANAGER')
enter_to_continue()
clear_screen()
menu = '0'
while menu != '6':
    print(menu_dict['m1'])
    menu = input('Enter menu number: ')
    clear_screen()
    if menu == '1':
        # menu Orders/Offers
        while menu != '9':
            print(menu_dict['m11'])
            menu = input('Enter menu number: ')
            clear_screen()
            if menu == '1':
                # open new order
                print('Open new order\n')
                car_vin, client_id, operations_list = get_values_for_new_order_offer(cars, clients, operations)
                if not car_vin or not client_id or not operations_list:
                    break
                new_order_offer = new_order_offer('orders.csv', Order, car_vin, client_id, operations_list)
                print(new_order_offer)
                enter_to_continue()
                clear_screen()
            elif menu == '2':
                # menu Open new offer
                print('Open new offer\n')
                car_vin, client_id, operations_list = get_values_for_new_order_offer(cars, clients, operations)
                if not car_vin or not client_id or not operations_list:
                    break
                new_order_offer = new_order_offer('offers.csv', Offer, car_vin, client_id, operations_list)
                print(new_order_offer)
                enter_to_continue()
                clear_screen()
            elif menu == '3':
                # menu Check order
                data_base = open_orders_file('orders.csv', OrdersArchive, Order)
                order_number = input('Enter order number: ')
                if not check_number(order_number, data_base):
                    break
                print(data_base[order_number])
                enter_to_continue()
                clear_screen()
                while menu != '5':
                    print(menu_dict['m113'])
                    menu = input('Enter menu number: ')
                    clear_screen()
                    if menu == '1':
                        # add operations in order
                        updated_order = add_del_operations('orders.csv', Order, order_number, 'add')
                        clear_screen()
                        print(f'Updated order:\n{updated_order}')
                        enter_to_continue()
                        clear_screen()
                    if menu == '2':
                        # delete operations from order
                        updated_order = add_del_operations('orders.csv', Order, order_number, 'delete')
                        clear_screen()
                        print(f'Updated order:\n{updated_order}')
                        enter_to_continue()
                        clear_screen()
                    if menu == '3':
                        # add/delete just parts
                        updated_order = add_delete_just_parts('orders.csv', Order, order_number)
                        clear_screen()
                        print(f'Updated order:\n{updated_order}')
                        enter_to_continue()
                        clear_screen()
                    if menu == '4':
                        # close order
                        question = input(f'Do you want to close order {order_number}? [Y/N] :')
                        if question in ('Y', 'y'):
                            closed_order = close_order_offer('orders.csv', Order, order_number)
                            clear_screen()
                            print(f'The order {order_number} has been closed, '
                                  f'it can not longer be modified\n\n{closed_order}')
                            enter_to_continue()
                        clear_screen()
                menu = '0'
            elif menu == '4':
                # menu Check offer
                data_base = open_orders_file('offers.csv', OrdersArchive, Offer)
                offer_number = input('Enter offer number: ')
                if not check_number(offer_number, data_base):
                    break
                print(data_base[offer_number])
                enter_to_continue()
                clear_screen()
                while menu != '5':
                    print(menu_dict['m114'])
                    menu = input('Enter menu number: ')
                    clear_screen()
                    if menu == '1':
                        # add operations in offer
                        updated_offer = add_del_operations('offers.csv', Offer, offer_number, 'add')
                        clear_screen()
                        print(f'Updated offer:\n{updated_offer}')
                        enter_to_continue()
                        clear_screen()
                    if menu == '2':
                        # delete operations from offer
                        updated_offer = add_del_operations('offers.csv', Offer, offer_number, 'delete')
                        clear_screen()
                        print(f'Updated offer:\n{updated_offer}')
                        enter_to_continue()
                        clear_screen()
                    if menu == '3':
                        # add/delete just parts
                        updated_offer = add_delete_just_parts('offers.csv', Offer, offer_number)
                        clear_screen()
                        print(f'Updated offer:\n{updated_offer}')
                        enter_to_continue()
                        clear_screen()
                    if menu == '4':
                        # close offer
                        question = input(f'Do you want to close offer {offer_number}? [Y/N] :')
                        if question in ('Y', 'y'):
                            closed_offer = close_order_offer('offers.csv', Offer, offer_number)
                            clear_screen()
                            print(f'The offer {offer_number} has been closed, '
                                  f'it can not longer be modified\n\n{closed_offer}')
                            enter_to_continue()
                        clear_screen()
                # menu = '0'
            elif menu == '5':
                # add two orders
                data_base = open_orders_file('orders.csv', OrdersArchive, Order)
                first_order_number = input('Enter the number for the first order: ')
                if not check_number(first_order_number, data_base):
                    break
                second_order_number = input('Enter the number for the second order: ')
                if not check_number(second_order_number, data_base):
                    break
                result_order = add_two_orders('orders.csv', Order, first_order_number, second_order_number)
                print(f'The result order:\n\n{result_order}')
                enter_to_continue()
                clear_screen()
            elif menu == '6':
                # print orders/offers by car vin and status
                print('OFFER / ORDER BY CAR AND STATUS\n')
                document_type = input(f'ORDER/OFFER\n1.Order\n2.Offer\nChoose type [1/2]: ')
                if document_type == '1':
                    orders_by_car = OrdersArchive()
                    vin, cl_id = get_values_for_filters(cars, None)
                    if not vin:
                        break
                    status = input(f'STATUS\n1.Open\n2.Closed\nChoose status of the documents [open/closed/None]:')
                    status = status.lower()
                    if status not in ('open', 'closed', ''):
                        print(status)
                        print(type(status))
                        print('Wrong choice !!!')
                        enter_to_continue()
                        break
                    orders_by_car_gen = sort_orders_by_car_or_client_generator('orders.csv', Order, car_vin=vin,
                                                                               client_id=cl_id, status=status)
                    for order in orders_by_car_gen:
                        save_from_file(order, orders_by_car)
                    print(orders_by_car)
                    enter_to_continue()
                    clear_screen()
                elif document_type == '2':
                    offers_by_car = OrdersArchive()
                    vin, cl_id = get_values_for_filters(cars, None)
                    if not vin:
                        break
                    status = input(f'STATUS\n1.Open\n2.Closed\nChoose status of the documents [open/closed/None]:')
                    status = status.lower()
                    if status not in ('open', 'closed', ''):
                        print(status)
                        print(type(status))
                        print('Wrong choice !!!')
                        enter_to_continue()
                        break
                    offers_by_car_gen = sort_orders_by_car_or_client_generator('offers.csv', Offer, car_vin=vin,
                                                                               client_id=cl_id, status=status)
                    for offer in offers_by_car_gen:
                        save_from_file(offer, offers_by_car)
                    print(offers_by_car)
                    enter_to_continue()
                    clear_screen()
                else:
                    clear_screen()
            elif menu == '7':
                # print orders/offers by client id and status
                print('OFFER / ORDER BY CLIENT AND STATUS\n')
                document_type = input(f'ORDER/OFFER\n1.Order\n2.Offer\nChoose type [1/2]: ')
                if document_type == '1':
                    orders_by_client = OrdersArchive()
                    vin, cl_id = get_values_for_filters(None, clients)
                    print(cl_id)
                    if not cl_id:
                        break
                    status = input(f'STATUS\n1.Open\n2.Closed\nChoose status of the documents [open/closed/None]:')
                    status = status.lower()
                    if status not in ('open', 'closed', ''):
                        print(status)
                        print(type(status))
                        print('Wrong choice !!!')
                        enter_to_continue()
                        break
                    orders_by_client_gen = sort_orders_by_car_or_client_generator('orders.csv', Order, car_vin=vin,
                                                                                  client_id=cl_id, status=status)
                    for order in orders_by_client_gen:
                        save_from_file(order, orders_by_client)
                    print(orders_by_client)
                    enter_to_continue()
                    clear_screen()
                elif document_type == '2':
                    offers_by_client = OrdersArchive()
                    vin, cl_id = get_values_for_filters(None, clients)
                    if not vin:
                        break
                    status = input(f'STATUS\n1.Open\n2.Closed\nChoose status of the documents [open/closed/None]:')
                    status = status.lower()
                    if status not in ('open', 'closed', ''):
                        print(status)
                        print(type(status))
                        print('Wrong choice !!!')
                        enter_to_continue()
                        break
                    offers_by_client_gen = sort_orders_by_car_or_client_generator('offers.csv', Offer, car_vin=vin,
                                                                                  client_id=cl_id, status=status)
                    for offer in offers_by_client_gen:
                        save_from_file(offer, offers_by_client)
                    print(offers_by_client)
                    enter_to_continue()
                    clear_screen()
                else:
                    clear_screen()
            elif menu == '8':
                # print orders/offers betwin two dates status
                print('OFFER / ORDER BETWIN TWO DATES BY ID AND STATUS\n')
                document_type = input(f'ORDER/OFFER\n1.Order\n2.Offer\nChoose type [1/2]: ')
                if document_type == '1':
                    status = input(f'STATUS\n1.Open\n2.Closed\nChoose status of the documents [open/closed/None]:')
                    status = status.lower()
                    if status not in ('open', 'closed', ''):
                        print(status)
                        print(type(status))
                        print('Wrong choice !!!')
                        enter_to_continue()
                    start_date = str(input('Start date (if empty filter from first day)[y m d]: '))
                    end_date = str(input('End date (if empty filter until today)[y m d]: '))
                    orders_from_date_gen = orders_betwin_dates_generator('orders.csv', start_date, end_date,
                                                                         Order, status=status)
                    orders_from_date = OrdersArchive()
                    for order in orders_from_date_gen:
                        save_from_file(order, orders_from_date)
                    print(orders_from_date)
                    enter_to_continue()
                    clear_screen()
                elif document_type == '2':
                    offers_by_client = OrdersArchive()
                    vin, cl_id = get_values_for_filters(None, clients)
                    if not vin:
                        break
                    status = input(f'STATUS\n1.Open\n2.Closed\nChoose status of the documents [open/closed/None]:')
                    status = status.lower()
                    if status not in ('open', 'closed', ''):
                        print(status)
                        print(type(status))
                        print('Wrong choice !!!')
                        enter_to_continue()
                        break
                    start_date = str(input('Start date (if empty filter from first day)[y m d]: '))
                    end_date = str(input('End date (if empty filter until today)[y m d]: '))
                    offers_from_date_gen = orders_betwin_dates_generator('offers.csv', start_date, end_date,
                                                                         Offer, status=status)
                    offers_from_date = OrdersArchive()
                    for offer in offers_from_date_gen:
                        save_from_file(offer, offers_from_date)
                    print(offers_from_date)
                    enter_to_continue()
                    clear_screen()
                else:
                    clear_screen()
        menu = '0'
    elif menu == '2':
        # menu Cars
        while menu != '5':
            print(menu_dict['m12'])
            menu = input('Enter menu number: ')
            clear_screen()
            if menu == '1':
                # add new car
                pass
            if menu == '2':
                # print car by vin
                pass
            if menu == '3':
                # Search car by registration number
                pass
            if menu == '4':
                # Print all cars
                print(cars)
                enter_to_continue()
                clear_screen()
    elif menu == '3':
        # menu Clients
        while menu != '5':
            print(menu_dict['m13'])
            menu = input('Enter menu number: ')
            clear_screen()
            if menu == '1':
                # add new client
                pass
            if menu == '2':
                # print client by client id
                pass
            if menu == '3':
                # Search car by name
                pass
            if menu == '4':
                # Print all clients
                print(clients)
                enter_to_continue()
                clear_screen()

    elif menu == '4':
        # menu Operations
        menu = '0'
        while menu != '4':
            print(menu_dict['m14'])
            menu = input('Enter menu number: ')
            clear_screen()
            if menu == '1':
                # add new operation
                pass
            if menu == '2':
                # search operation by keyword
                pass
            if menu == '3':
                # print all operations
                print(operations)
                enter_to_continue()
                clear_screen()
    elif menu == '5':
        # menu Spare Parts
        menu = '0'
        while menu != '4':
            print(menu_dict['m15'])
            menu = input('Enter menu number: ')
            clear_screen()
            if menu == '1':
                # search spare part by part code
                pass
            if menu == '2':
                # search spare part by keyword
                pass
            if menu == '3':
                # print all spare parts
                pprint(parts)
                enter_to_continue()
                clear_screen()
