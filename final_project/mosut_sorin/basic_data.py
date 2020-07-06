import csv
import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)
module_name = '<< {} >> '.format(__name__)


class CarClient:

    def __init__(self, id_no, *args, data_base=None):
        if id_no in data_base:
            raise Exception('Duplicate id_no')
        self._data_list = [id_no, *args]

    def __str__(self):
        print_string = f'{self._data_list}'
        return print_string

    def __iter__(self):
        return iter(self._data_list)

    def __len__(self):
        return len(self._data_list)

    def __getitem__(self, index):
        return self._data_list[index]


class Car(CarClient):

    def __init__(self, id_no, *args, data_base=None):
        super().__init__(id_no, *args, data_base=data_base)
        self.vin_number = id_no

    @property
    def vin_number(self):
        return self.__vin_number

    @vin_number.setter
    def vin_number(self, value):
        if len(value) == 17:
            self.__vin_number = value.upper()
        else:
            raise ValueError('vin number must have 17 lenght')


class Client(CarClient):

    def __init__(self, id_no, *args, data_base=None):
        super().__init__(id_no, *args, data_base=data_base)
        self.client_id = id_no


class CarsDataBase:

    def __init__(self):
        self._data_dict = {}

    def __str__(self):
        print_string = ''
        for key, value in self._data_dict.items():
            print_string = ''.join((print_string, f'{key}: {value}', '\n'))
        return print_string

    def __iter__(self):
        return iter(self._data_dict)

    def __len__(self):
        return len(self._data_dict)

    def __getitem__(self, item):
        return self._data_dict[item]

    def contains_check(self, item):
        if item in self._data_dict.keys():
            return True
        else:
            raise Exception(f'No item with {item} identification number in data base !!!')

    def keys(self):
        return self._data_dict.keys()

    def values(self):
        return self._data_dict.values()

    def items(self):
        return self._data_dict.items()

    def update(self, item):
        self._data_dict.update(
            {
                item[0]: item[1: len(item)]
            }
        )

    def search(self, search_data):
        search_results = []
        for key, value in self._data_dict.items():
            if search_data in value:
                search_results.append(key)
        return search_results


class ClientsDataBase(CarsDataBase):

    def search(self, search_data):
        search_results = []
        for key, value in self._data_dict.items():
            if search_data in value:
                search_results.append(key)
        return search_results


class Operation:

    def __init__(self, operation_title, operation_labor_time, operation_parts):
        self.title = operation_title
        self.labor_time = operation_labor_time
        self.parts = {}
        self.parts, self.parts_cost = create_parts_dict(operation_parts, self.parts)
        self.labor_cost = self.labor_time * rate
        self.total_cost = self.labor_cost + self.parts_cost

    def __str__(self):
        print_string = f'{self.title} - Labor Time: {self.labor_time}h - Labor Cost: {self.labor_cost}ron - ' \
                       f'Parts Cost: {self.parts_cost} - Total Cost: {self.total_cost}: \n'
        parts_string = ''
        for key, values in self.parts.items():
            parts_string = ''.join((parts_string, f'{" " * 20}{key} - {values}\n'))
        print_string = ''.join((print_string, parts_string))
        return print_string

    def __iter__(self):
        return iter(self.parts)

    def __getitem__(self, item):
        return self.parts.values[item]

    def __contains__(self, item):
        return item in self.title

    def values(self):
        return self.parts.values()


class OperationsDataBase:

    def __init__(self):
        self._operations = []

    def __str__(self):
        print_string = ''
        for item in self._operations:
            print_string = ''.join((print_string, f'{item}\n'))
        return print_string

    def __iter__(self):
        return iter(self._operations)

    def __getitem__(self, index):
        return self._operations[index]

    def contains_check(self, item):
        titles = []
        for oper in self:
            titles.append(oper.title)
        if item in titles:
            return True
        else:
            raise Exception(f'No operation named {item} in data base !!!')

    def append(self, item):
        self._operations.append(item)

    def search(self, key_word):
        search_operations_resuls = OperationsDataBase()
        for operation in self._operations:
            if key_word in operation.title:
                search_operations_resuls.append(operation)
        return search_operations_resuls


def open_cars_file(file, data_base_class):
    with open(file, 'r') as file:
        data_base = data_base_class()
        data_base_from_file = pd.read_csv(file, delimiter=',')
        zipp = zip(data_base_from_file['vin'], data_base_from_file['reg_no'], data_base_from_file['brand'],
                   data_base_from_file['model'],
                   data_base_from_file['cmc'], data_base_from_file['kw'], data_base_from_file['year'])
        for row in zipp:
            vin, reg_no, brand, model, cmc, kw, year = row
            car_from_file = build_car_client_instance(Car, str(vin), reg_no, brand, model, cmc, kw, year,
                                                      data_base=data_base)
            save_instance(car_from_file, data_base)
    logger.debug('creating data base from file {}:\n'.format(file, data_base))
    return data_base


def open_clients_file(file, data_base_class):
    with open(file, 'r') as file:
        data_base = data_base_class()
        data_base_from_file = pd.read_csv(file, delimiter=',')
        zipp = zip(data_base_from_file['client_id'], data_base_from_file['client_name'],
                   data_base_from_file['client_adress'])
        for row in zipp:
            client_id, name, adress = row
            client_from_file = build_car_client_instance(Client, str(client_id), name, adress, data_base=data_base)
            save_instance(client_from_file, data_base)
    return data_base


def open_parts_file(file):
    with open(file, 'r') as file:
        data_base_from_file = pd.read_csv(file, delimiter=',')
        zipp = zip(data_base_from_file['code'], data_base_from_file['name'],
                   data_base_from_file['brand'], data_base_from_file['cost'])
        data_base = {
            row[0]: [row[1], row[2], float(row[3])]
            for row in zipp
        }
    return data_base


def cars_file_header(file):
    file_size = os.stat(file).st_size
    if file_size == 0:
        with open(file, 'w') as file:
            header = ['vin', 'reg_no', 'brand', 'model', 'cmc', 'kw', 'year']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
        return True


def write_in_cars_file(file, data_base):
    if data_base:
        with open(file, 'a') as file:
            header = ['vin', 'reg_no', 'brand', 'model', 'cmc', 'kw', 'year']
            writer = csv.DictWriter(file, fieldnames=header)
            for key, value in data_base.items():
                writer.writerow(
                    {
                        'vin': key.upper(),
                        'reg_no': value[0].upper(),
                        'brand': value[1].title(),
                        'model': value[2].title(),
                        'cmc': value[3],
                        'kw': value[4],
                        'year': value[5]
                    }
                )
        return True


def clients_file_header(file):
    file_size = os.stat(file).st_size
    if file_size == 0:
        with open(file, 'w') as file:
            header = ['client_id', 'client_name', 'client_adress']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
        return True


def write_in_clients_file(file, data_base):
    if data_base:
        with open(file, 'a') as file:
            header = ['client_id', 'client_name', 'client_adress']
            writer = csv.DictWriter(file, fieldnames=header)
            for key, value in data_base.items():
                writer.writerow(
                    {
                        'client_id': key.upper(),
                        'client_name': value[0].upper(),
                        'client_adress': value[1].title()
                    }
                )
        return True


def build_car_client_instance(class_name, id_no, *args, data_base):
    try:
        id_no = id_no.upper()
        instance = class_name(id_no, *args, data_base=data_base)
        return instance
    except Exception as e:
        print(e)


def save_instance(obj, data_base):
    if obj:
        data_base.update(obj)
    return True


def create_parts_dict(parts_in, parts_dict):
    parts_cost = 0
    for part_code in parts_in.keys():
        parts_dict.update({part_code: [parts[part_code][0], parts[part_code][1], parts[part_code][2],
                                       parts_in[part_code], parts[part_code][2] * parts_in[part_code]]})
        parts_cost += parts[part_code][2] * parts_in[part_code]
    return parts_dict, parts_cost


def save_operation(operation, data_base):
    if operation:
        data_base.append(operation)
        return True


def get_results(fnc):
    def inner(search_item):
        ids_results, data_base = fnc(search_item)
        if not ids_results:
            print(f'In {data_base.class_name} , {search_item} is not registrated')
        else:
            return ids_results

    return inner


@get_results
def search_client_by_name(name):
    clients_result = clients.search(name)
    return clients_result, clients


@get_results
def search_car_by_reg_number(reg_number):
    cars_result = cars.search(reg_number)
    return cars_result, cars


logger.info('basic data preparation')
rate = 100
cars_for_append = CarsDataBase()
clients_for_append = ClientsDataBase()

cars_file_header('cars.csv')
clients_file_header('clients.csv')

parts = open_parts_file('parts.csv')

operations = OperationsDataBase()

engine_oil_replace_parts = {'cas1523': 5,
                            'mahu2525': 1,
                            'bbu447': 1
                            }
engine_oil_replace = Operation('Engine Oil Replace', 1.5, engine_oil_replace_parts)
save_operation(engine_oil_replace, operations)

brake_discs_replace_parts = {
    'tex874': 2,
    'tex558': 1,
    'tex689': 1
}
brake_discs_replace = Operation('Brake Discs Replace', 2, brake_discs_replace_parts)
save_operation(brake_discs_replace, operations)

brake_pads_replace_parts = {
    'tex558': 1,
    'tex689': 1
}
brake_pads_replace = Operation('Brake Pads Replace', 1.6, brake_pads_replace_parts)
save_operation(brake_pads_replace, operations)

logger.info('data base files')
cars = open_cars_file('cars.csv', CarsDataBase)
clients = open_clients_file('clients.csv', ClientsDataBase)
