from final_project.mosut_sorin.basic_data import *
from collections import Counter
from ast import literal_eval
import datetime
import time


class PrintFormatMixin:

    def __str__(self):

        operations_string, just_parts = '', ''
        for operation in self.operations:
            operations_string = ''.join((operations_string, f'{" " * 15}{operation}\n'))
        for part_code, part_details in self.just_parts.items():
            just_parts = ''.join((just_parts, f'{" " * 15}{part_details[0]}: {part_code}, {part_details[1:]}\n'))

        print_value = f' {"_" * 119}\n|{" " * 119}|\n' \
                      f'| MPower Auto Shop{" " * 102}|\n' \
                      f'| Work Order{" " * 54}Order no.{" " * 5}Offer no.{" " * 5}Open date{" " * 5}Close date  |\n' \
                      f'|{" " * 65}{self.order_number}{" " * 5}' \
                      f'{self.offer_number + (" " * 2) if self.offer_number else " " * 13}' \
                      f' {self.open_date[:10]}' \
                      f'{(" " * 4) + self.close_date[:10] if self.close_date else (" " * 7) + "Open" + "   "}  |\n' \
                      f'|{"-" * 119}|\n' \
                      f' ' \
                      f'{" " * 10}Car:\n{" " * 15}{self._car}\n{" " * 10}Client:\n{" " * 15}{self._client}\n\n' \
                      f'{" " * 10}Operations:\n{operations_string}{" " * 10}Free Operation Parts:\n{just_parts}\n' \
                      f'{" " * 10}Total:\n{" " * 15}Total Order labor time: {self.total_labor_time} h\n' \
                      f'{" " * 15}Total Order Labor Cost: {self.total_labor_cost} ron\n' \
                      f'{" " * 15}Total Order Parts Cost: ' \
                      f'{self.total_parts_cost} ron\n' \
                      f'{" " * 15}Total Free Operation Parts Cost: {self.just_parts_cost} ron\n' \
                      f'{" " * 15}Total Order Cost: {self.total_cost} ron\n'
        return print_value

    def __repr__(self):
        operations_string, just_parts = '', ''
        for operation in self.operations:
            operations_string = ''.join((operations_string, f'{" " * 15}{operation}\n'))
        for part_code, part_details in self.just_parts.items():
            just_parts = ''.join((just_parts, f'{" " * 15}{part_details[0]}: {part_code}, {part_details[1:]}\n'))
        print_value = f'{self.order_number}{" - " + self.offer_number if self.offer_number else ""}:\n' \
                      f'{" " * 10}' \
                      f'Open: {self.open_date} - Closed: {self.close_date if self.close_date else "Open"}\n' \
                      f'{" " * 10}Car:\n{" " * 15}{self._car}\n{" " * 10}Client:\n{" " * 15}{self._client}\n\n' \
                      f'{" " * 10}Operations:\n{operations_string}{" " * 10}Free Operation Parts:\n{just_parts}\n' \
                      f'{" " * 10}Total:\n{" " * 15}Total Order labor time: {self.total_labor_time} h\n' \
                      f'{" " * 15}Total Order Labor Cost: {self.total_labor_cost} ron\n' \
                      f'{" " * 15}Total Order Parts Cost: ' \
                      f'{self.total_parts_cost} ron\n' \
                      f'{" " * 15}Total Free Operation Parts Cost: {self.just_parts_cost} ron\n' \
                      f'{" " * 15}Total Order Cost: {self.total_cost} ron\n'

        return print_value


class OfferOrderStructure(PrintFormatMixin):
    def __init__(self, vin, client_id, operations_titles_list, main_number, open_time_seconds):
        self.order_number = main_number
        self.open_time_seconds = open_time_seconds
        self.open_date = time.strftime('%d %m %Y %H:%M', time.gmtime(self.open_time_seconds))
        self.close_date = self.close_date
        self.vin = vin
        self._car = {vin: cars[self.vin]}
        self.client_id = client_id
        self._client = {client_id: clients[self.client_id]}
        self.operations_titles = operations_titles_list
        self.operations = []
        self.operations = operations_to_order(self.operations_titles, self.operations)
        self.just_parts = {}
        self.total_labor_time = 0
        self.total_labor_cost = 0
        self.total_parts_cost = 0
        self.total_cost = 0
        self.just_parts_cost = 0

    def check_status(self):
        if self.close_date:
            raise Exception('This order has been closed, can not change the details')
        else:
            return 'open'

    # save method adds the updated order or offer in the proper data base
    def save(self, data_base):
        try:
            self.check_status()
            self.calculate_costs()
            data_base.update(self)
        except Exception as e:
            print(e)
        finally:
            return True

    def save_from_file(self, data_base):
        self.calculate_costs()
        data_base.update(self)
        return True

    def close(self):
        try:
            self.check_status()
            time_now = time.localtime()
            self.close_date = time.strftime('%d %m %Y %H:%M', time_now)
        except Exception as e:
            print(e)
        finally:
            return True

    def calculate_costs(self):
        self.total_labor_time = 0
        self.total_labor_cost = 0
        self.total_parts_cost = 0
        self.total_cost = 0
        self.just_parts_cost = 0
        for operation in self.operations:
            self.total_labor_time += operation.labor_time
            self.total_labor_cost += operation.labor_cost
            self.total_parts_cost += operation.parts_cost
            self.total_cost += operation.total_cost
        for part_details in self.just_parts.values():
            self.just_parts_cost += part_details[4]
        self.total_cost += self.just_parts_cost

    def remove_operation(self, operation_title):
        for operation in self.operations:
            if operation_title == operation.title:
                self.operations.remove(operation)
                self.operations_titles.remove(operation.title)
                return True

    def add_delete(self, operations_titles_list, flag):
        try:
            self.check_status()
            if flag == 'delete':
                for operation_title in operations_titles_list:
                    self.remove_operation(operation_title)
            elif flag == 'add':
                self.operations = operations_to_order(operations_titles_list, self.operations)
                self.operations_titles += operations_titles_list
        except Exception as e:
            print(e)
        finally:
            return self

    def add_just_parts(self, just_parts_dict):
        if self.just_parts:
            for part_code, part_details in just_parts_dict.items():
                if part_code in self.just_parts.keys():
                    self.just_parts[part_code][3] += just_parts_dict[part_code][3]
                    self.just_parts[part_code][4] += just_parts_dict[part_code][4]
                    if self.just_parts[part_code][3] < 0:
                        self.just_parts.pop(part_code)
                else:
                    self.just_parts.update({part_code: part_details})
            return self
        else:
            self.just_parts.update(just_parts_dict)
            return self

    def add_just_parts_file(self, just_parts_dict):
        self.just_parts.update(just_parts_dict)
        return self


class Order(OfferOrderStructure):

    def __init__(self, vin, client_id, operations_titles_list, main_number, open_time, close_date=None,
                 second_number=None):
        self.order_number = main_number
        self.offer_number = second_number
        self.close_date = close_date
        super().__init__(vin, client_id, operations_titles_list, main_number, open_time)

    def __iter__(self):
        return iter(self.operations)

    def add_check(self, other):
        if self.vin != other.vin or self.client_id != other.client_id:
            raise Exception('Can not combine two oreders for different car or client')
        else:
            return True

    def __add__(self, other):
        try:
            self.add_check(other)
            vin_number = self.vin
            client_id = self.client_id
            operations_list = self.operations_titles + other.operations_titles
            sum_order = open_new_order_offer(Order, vin_number, client_id, operations_list, orders)
            just_parts_dict_obj_1 = {key: value[3] for key, value in self.just_parts.items()}
            just_parts_dict_obj_2 = {key: value[3] for key, value in other.just_parts.items()}
            just_parts_dict = dict(Counter(just_parts_dict_obj_1) + Counter(just_parts_dict_obj_2))
            add_just_parts(sum_order, just_parts_dict, parts)
            save_order_offer(sum_order, orders)
            self.close()
            other.close()
            return sum_order
        except Exception as exception:
            print(exception)


class OrdersArchive:

    def __init__(self, order=None):
        self.total_labor_time = 0
        self.total_labor_cost = 0
        self.total_parts_cost = 0
        self.total_just_parts_cost = 0
        self.total_cost = 0
        if order:
            self._orders_archive = {order.order_number: order}
        else:
            self._orders_archive = {}

    def __str__(self):
        print_value = ''
        for order in self._orders_archive.values():
            operations_string, just_parts_string = '', ''
            for operation in order.operations:
                operations_string = ''.join((operations_string, f'{" " * 15}{operation}\n'))
            for part_code, part_details in order.just_parts.items():
                just_parts_string = ''.join(
                    (just_parts_string, f'{" " * 15}{part_details[0]}: {part_code}, {part_details[1:]}\n'))
            order_print_attr = f'\n{order.order_number}: {order.open_date} - ' \
                               f'{order.close_date if order.close_date else "Open"}, ' \
                               f'{order.vin}, {order.client_id}\n' \
                               f'{" " * 10}Operations:\n{operations_string}' \
                               f'{" " * 10}Free Operation Parts:\n{just_parts_string}' \
                               f'{" " * 10}LT: {order.total_labor_time} - LC: {order.total_labor_cost} - ' \
                               f'OP: {order.total_parts_cost}' \
                               f' - FP: {order.just_parts_cost} - TOTAL: {order.total_cost}\n'
            print_value = ''.join((print_value, order_print_attr))
        order_costs = f'\n{" " * 5}Total Labour Time {self.total_labor_time}\n' \
                      f'{" " * 5}Total Labour Cost {self.total_labor_cost}\n' \
                      f'{" " * 5}Total Parts Cost {self.total_parts_cost}\n' \
                      f'{" " * 5}Total Free Operation Parts Cost {self.total_just_parts_cost}' \
                      f'\n{" " * 5}Total Cost {self.total_cost}'
        print_value = ''.join((print_value, order_costs))
        return print_value

    def __iter__(self):
        return iter(self._orders_archive.keys())

    def __len__(self):
        return len(self._orders_archive)

    def __getitem__(self, item):
        return self._orders_archive[item]

    def __contains__(self, item):
        if item in self._orders_archive.keys():
            return True
        else:
            raise Exception(f'No order or offer with {item} number, in data base !!!')

    def keys(self):
        return self._orders_archive.keys()

    def values(self):
        return self._orders_archive.values()

    def items(self):
        return self._orders_archive.items()

    def latest(self):
        if self._orders_archive:
            orders_number_list = [int(order_number[-9:]) for order_number in self]
            orders_number_list.sort()
            latest_number = str(orders_number_list[-1])
        else:
            latest_number = None

        return latest_number

    def update(self, order):
        self._orders_archive.update({order.order_number: order})
        self.update_total_values()

    def update_total_values(self):
        self.total_labor_time = 0
        self.total_labor_cost = 0
        self.total_parts_cost = 0
        self.total_just_parts_cost = 0
        self.total_cost = 0
        for order in self._orders_archive.values():
            self.total_labor_time += order.total_labor_time
            self.total_labor_cost += order.total_labor_cost
            self.total_parts_cost += order.total_parts_cost
            self.total_just_parts_cost += order.just_parts_cost
            self.total_cost = self.total_labor_cost + self.total_parts_cost + self.total_just_parts_cost


class Offer(OfferOrderStructure):

    def __init__(self, vin, client_id, operations_titles_list, main_number, open_time, close_date=None,
                 second_number=None):
        self.close_date = close_date
        super().__init__(vin, client_id, operations_titles_list, main_number, open_time)
        if str(main_number)[0:2] != 'OF':
            self.order_number = ''.join(('OF', main_number))
        else:
            self.order_number = main_number
        self.operations_titles = operations_titles_list
        self.offer_number = second_number

    def __str__(self):
        operations_string = ''
        for operation in self.operations:
            operations_string = ''.join((operations_string, f'{" " * 15}{operation}\n'))
        just_parts = ''
        for part_code, part_details in self.just_parts.items():
            just_parts = ''.join((just_parts, f'{" " * 15}{part_details[0]}: {part_code}, {part_details[1:]}\n'))
        print_value = f'{self.order_number}:\n' \
                      f'{" " * 10}' \
                      f'Open: {self.open_date} - Closed: {self.close_date if self.close_date else "Open"}\n' \
                      f'{" " * 10}Car:\n{" " * 15}{self._car}\n{" " * 10}Client:\n{" " * 15}{self._client}\n\n' \
                      f'{" " * 10}Operations:\n{operations_string}{" " * 10}Free Operation Parts:\n{just_parts}\n' \
                      f'{" " * 10}Total:\n{" " * 15}Total Order labor time: {self.total_labor_time} h\n' \
                      f'{" " * 15}Total Order Labor Cost: {self.total_labor_cost} ron\n' \
                      f'{" " * 15}Total Order Parts Cost: ' \
                      f'{self.total_parts_cost} ron\n' \
                      f'{" " * 15}Total Free Operation Parts Cost: {self.just_parts_cost} ron\n' \
                      f'{" " * 15}Total Order Cost: {self.total_cost} ron\n'

        return print_value


def unique_number_genrator(data_base):
    open_time = time.localtime()
    open_time_seconds = time.mktime(open_time)
    open_date = time.strftime('%d %m %Y %H:%M', open_time)
    unique_number_date = f'{open_date[8: 10]}{open_date[3: 5]}{open_date[0: 2]}'
    if data_base.latest():
        latest = data_base.latest()
        if latest[-9:-3] == unique_number_date:
            unique_number = str(int(latest) + 1)
        else:
            unique_number = ''.join((unique_number_date, '001'))
    else:
        unique_number = ''.join((unique_number_date, '001'))

    return unique_number, open_time_seconds


def open_new_order_offer(class_constructor, vin_number, client_id, operations_list, data_base):
    vin_number = vin_number.upper()
    client_id = client_id.upper()
    unique_order_number, open_order_time = unique_number_genrator(data_base)
    order = class_constructor(vin_number, client_id, operations_list, unique_order_number, open_order_time)
    return order


def operations_to_order(operations_titles_list, operations_list):
    for operation_title in operations_titles_list:
        for operation in operations:
            # identify the operations called for this order in the operations data base
            if operation_title in operation:
                operations_list.append(operation)

    return operations_list


def save_order_offer(order, data_base):
    if order:
        order.save(data_base)
        return order.save(data_base)


def save_from_file(order, data_base):
    if order:
        order.save_from_file(data_base)
        return True


def add_delete_operation(order_to_update, operations_titles_list, flag):
    if order_to_update:
        order_to_update.add_delete(operations_titles_list, flag)
        return order_to_update


def add_just_parts(order, just_parts_input_dict, parts_data_base):
    try:
        order.check_status()
        just_parts_full_dict = {}
        for part_code, pieces in just_parts_input_dict.items():
            part_details = parts_data_base[part_code]
            part_cost = part_details[2]
            part_pieces_cost = [pieces, pieces * part_cost]
            parts_details_order = part_details + part_pieces_cost
            just_parts_full_dict.update({part_code: parts_details_order})
        updated_order = order.add_just_parts(just_parts_full_dict)
        return updated_order
    except Exception as e:
        print(e)
        return order


def add_just_parts_from_file(order, just_parts_input_dict, parts_data_base):
    just_parts_full_dict = {}
    for part_code, pieces in just_parts_input_dict.items():
        part_details = parts_data_base[part_code]
        part_cost = part_details[2]
        part_pieces_cost = [pieces, pieces * part_cost]
        parts_details_order = part_details + part_pieces_cost
        just_parts_full_dict.update({part_code: parts_details_order})
    updated_order = order.add_just_parts(just_parts_full_dict)
    return updated_order


def offer_to_order(offer, data_base):
    number = offer.order_number
    car_vin = offer.vin
    client_id = offer.client_id
    operations_list = offer.operations_titles
    order_from_offer = open_new_order_offer(Order, car_vin, client_id, operations_list, data_base)
    offer.close()
    offer.offer_number = order_from_offer.order_number
    order_from_offer.offer_number = number
    return order_from_offer


def seconds_from_date(date):
    year, month, day = [int(item) for item in date.split(' ')]
    date_time = datetime.datetime(year, month, day, 3, 0)
    seconds = time.mktime(date_time.timetuple())
    return seconds


def create_order_for_generator(row, instance_class):
    # operations_titles_list = ''
    order_number, vin_number, client_id, operations_list, just_parts_dict, open_time, close_date, offer_number = row
    order_number = str(order_number)
    client_id = str(client_id)
    operations_titles_list = operations_list.split('|')
    just_parts_dict = literal_eval(just_parts_dict)  # buid dict from string
    offer_number = str(offer_number)
    if str(close_date) == 'nan':
        close_date = None
    if str(offer_number) == 'nan':
        offer_number = None
    order = instance_class(vin_number, client_id, operations_titles_list, order_number, open_time,
                           close_date=close_date, second_number=offer_number)
    order = add_just_parts(order, just_parts_dict, parts)
    order.calculate_costs()
    return order


def orders_betwin_dates_generator(file, start_date, end_date, instance_class, status=None):
    header_main_number, header_second_number = file_title_check(file)
    if start_date == '':
        init_seconds = 0
    else:
        init_seconds = seconds_from_date(start_date)
    if end_date == '':
        now = time.localtime()
        fin_seconds = time.mktime(now)
    else:
        fin_seconds = seconds_from_date(end_date)
    with open(file, 'r') as file:
        data_base_from_file = pd.read_csv(file, delimiter=',')
        zipp = zip(data_base_from_file[header_main_number], data_base_from_file['vin_number'],
                   data_base_from_file['client_id'],
                   data_base_from_file['operations_list'], data_base_from_file['just_parts_dict'],
                   data_base_from_file['open_time'],
                   data_base_from_file['close_date'], data_base_from_file[header_second_number])
        for row in zipp:
            open_time_seconds = row[5]
            close_date = row[6]
            if init_seconds < int(open_time_seconds) < fin_seconds:
                if not status:
                    order = create_order_for_generator(row, instance_class)
                    yield order

                elif status == 'open' and str(close_date) == 'nan':
                    order = create_order_for_generator(row, instance_class)
                    yield order

                elif status == 'closed' and str(close_date) != 'nan':
                    order = create_order_for_generator(row, instance_class)
                    yield order


def sort_orders_by_car_or_client_generator(file, instance_class, car_vin=None, client_id=None, status=None):
    header_main_number, header_second_number = file_title_check(file)
    with open(file, 'r') as file:
        data_base_from_file = pd.read_csv(file, delimiter=',')
        zipp = zip(data_base_from_file[header_main_number], data_base_from_file['vin_number'],
                   data_base_from_file['client_id'],
                   data_base_from_file['operations_list'], data_base_from_file['just_parts_dict'],
                   data_base_from_file['open_time'],
                   data_base_from_file['close_date'], data_base_from_file[header_second_number])
        for row in zipp:
            car_vin_in_data_base = row[1]
            client_id_in_data_base = str(row[2])
            close_date = row[6]
            if car_vin == car_vin_in_data_base or client_id == client_id_in_data_base:
                if not status:
                    order = create_order_for_generator(row, instance_class)
                    yield order

                elif status == 'open' and str(close_date) == 'nan':
                    order = create_order_for_generator(row, instance_class)
                    yield order

                elif status == 'closed' and str(close_date) != 'nan':
                    order = create_order_for_generator(row, instance_class)
                    yield order


def file_title_check(file):
    file_name = file.title().lower()
    if 'order' in file_name:
        return ['order_number', 'offer_number']
    elif 'offer' in file_name:
        return ['offer_number', 'order_number']


def open_orders_file(file, class_for_data_base, instance_class):
    header_main_number, header_second_number = file_title_check(file)
    with open(file, 'r') as file:
        data_base = class_for_data_base()
        data_base_from_file = pd.read_csv(file, delimiter=',')
        zipp = zip(data_base_from_file[header_main_number], data_base_from_file['vin_number'],
                   data_base_from_file['client_id'],
                   data_base_from_file['operations_list'], data_base_from_file['just_parts_dict'],
                   data_base_from_file['open_time'],
                   data_base_from_file['close_date'], data_base_from_file[header_second_number])
        for row in zipp:
            main_number, vin, client_id, operations_list, just_parts_dict, open_time, close_date, second_number = row
            main_number = str(main_number)
            client_id = str(client_id)
            operations_list = str(operations_list).split('|')
            just_parts_dict = literal_eval(just_parts_dict)
            second_number = str(second_number)
            if str(close_date) == 'nan':
                close_date = None
            if str(second_number) == 'nan':
                second_number = None
            order = instance_class(vin, client_id, operations_list, main_number, open_time,
                                   close_date=close_date, second_number=second_number)
            add_just_parts_from_file(order, just_parts_dict, parts)
            save_from_file(order, data_base)
    return data_base


def write_in_file(file, data_base):
    header_main_number, header_second_number = file_title_check(file)
    try:
        if data_base:
            with open(file, 'w') as file:
                header = [header_main_number, 'vin_number', 'client_id', 'operations_list', 'just_parts_dict',
                          'open_time', 'close_date', header_second_number]
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()

                for key, value in data_base.items():
                    operations_titles_string = '|'.join(value.operations_titles)
                    just_parts = value.just_parts
                    just_parts_code_pieces = {key: value[3] for key, value in just_parts.items()}
                    just_parts_code_pieces_str = str(just_parts_code_pieces)

                    writer.writerow(
                        {
                            header_main_number: key,
                            'vin_number': value.vin,
                            'client_id': value.client_id,
                            'operations_list': operations_titles_string,
                            'just_parts_dict': just_parts_code_pieces_str,
                            'open_time': value.open_time_seconds,
                            'close_date': value.close_date,
                            header_second_number: value.offer_number
                        }
                    )
    except IOError:
        print('I/O Error')


logger.info('main data preparation')
orders = open_orders_file('orders.csv', OrdersArchive, Order)
offers = open_orders_file('offers.csv', OrdersArchive, Offer)
