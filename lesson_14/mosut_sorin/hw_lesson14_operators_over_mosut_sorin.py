"""
Lesson 14 - Operator Overloading
Challenge:
Design a class Challenge!
Create a Challenge similar to the ones we included in previous lessons. The challenge must touch the following points:
>      1. Try to present a real example inspired by your work or passions
>
>      2. Require operator overloading to solve at least one requirement of the challenge
>
>      3. At least one bonus, optional requirement
>
The challenge must contain any extra pieces of information that are required for completing the challenge such as
definition, logic diagrams, etc. The challenge will be written in the markdown format and saved in a .md file
Attach the solution of the challenge
"""

import time
from typing import List, Any, Union


class WorkOrder:  # Open Work Order

    _list_of_data: List[Union[Union[str, float], Any]]

    def __init__(self, registation, vin, brand, model, client, date_in=None, date_out=None, labor=0.0, parts_cost=0.0,
                 number=None):

        counter_wo_number = str(len(work_orders_dict) + len(work_orders_closed) + 1).rjust(3, '0') # counting all work shop orders
        time_now = time.localtime()
        date_today = time.strftime('%d %m %Y', time_now)

        if number:
            self.date_in = date_in
            self.wo_number = number
        if labor == 0 and not date_in and not number:
            self.wo_number = f'{date_today[8: 10]}{date_today[3: 5]}{date_today[0: 2]}{counter_wo_number}'
            self.date_in = date_today
        elif date_in and not number:
            self.date_in = date_in
            self.wo_number = f'{date_in[8: 10]}{date_in[3: 5]}{date_in[0: 2]}{counter_wo_number}'

        if date_out:
            self.date_out = date_today
        else:
            self.date_out = date_out

        self.registration = registation
        self.vin = vin
        self.brand = brand
        self.model = model
        self.client = client
        self.date_out = date_out
        self.labor = labor
        self.parts_cost = parts_cost
        self.labor_cost = labor * rate
        self.total_cost = self.parts_cost + self.labor_cost
        self._list_of_data = [self.wo_number, self.registration, self.vin, self.brand, self.model,
                              self.client, self.date_in, self.date_out, self.labor, self.parts_cost,
                              self.labor_cost, self.total_cost]

    def __str__(self):

        if self.date_out is None:
            date_out_print = 'open'
        else:
            date_out_print = self.date_out

        print_data = f'{self.wo_number} : {self.registration}, {self.vin}, {self.brand}, {self.model}, ' \
                     f'{self.client}, {self.date_in}, {date_out_print}, {self.labor:.2f} h, ' \
                     f'{self.parts_cost:.2f} ron, {self.labor_cost:.2f} ron, {self.total_cost:.2f} ron'

        return print_data

    def __iter__(self):
        return iter(self._list_of_data)

    def __len__(self):
        return len(self._list_of_data)

    def __getitem__(self, item):
        return self._list_of_data[item]

    def __contains__(self, item):
        return item in self._list_of_data


class WOByInputMixin:

    def __init__(self):
        self._wo_dict = {}

    def work_orders_by_input(self, input_data=None, car_or_client=None):
        wo_by_item_dict = WorkOrdersDict()
        out_data = [0, 0, 0, 0]  # empty list ready to get labor_time, labor_cost, parts_cost, total_cost
        for key in self._wo_dict:
            if car_or_client == 'car':

                item_no = 0
                if self._wo_dict[key][item_no] == input_data:
                    items_list = self._wo_dict[key]
                    wo_by_item_dict.update([[key, items_list]])
                    out_data = [sum(two_values) for two_values in zip(out_data, self._wo_dict[key][7: 11])]

            elif car_or_client == 'client':
                item_no = 4
                if self._wo_dict[key][item_no] == input_data:
                    items_list = self._wo_dict[key]
                    wo_by_item_dict.update([[key, items_list]])
                    out_data = [sum(two_values) for two_values in zip(out_data, self._wo_dict[key][7: 11])]

            else:
                raise ValueError('Valori incorecte')

        return wo_by_item_dict, out_data


class WorkOrdersDict(WOByInputMixin, dict):

    def __init__(self, item_in=None):
        super().__init__()
        self._wo_dict = {}
        if item_in:
            self.key = item_in[0]
            self.value = item_in[1:len(item_in)]
            self._wo_dict = {self.key: self.value}

    def __str__(self):
        print_dict = ''
        lenght_list = (7, 17, 12, 12, 16, 10, 10, 9, 9, 9, 9)
        ordered_keys_list = list(self._wo_dict.keys())
        ordered_keys_list.sort()

        for print_key in ordered_keys_list:
            item_and_lenght = zip(self._wo_dict[print_key], lenght_list)
            list_as_value = [str(value).center(lenght) for value, lenght in item_and_lenght]
            key_value_str = f'- {print_key} : {list_as_value}\n'
            print_dict = ''.join((print_dict, key_value_str))

        return print_dict

    def __iter__(self):
        return iter(self._wo_dict)

    def __len__(self):
        return len(self._wo_dict)

    def __setitem__(self, key, item):
        self._wo_dict[key] = item

    def __getitem__(self, key):
        return self._wo_dict[key]

    def __delitem__(self, key):
        if self._wo_dict[key][7] and self._wo_dict[key][8]:
            del self._wo_dict[key]
        else:
            raise ValueError('Missing values , instance can not be deleteted befor closing the work order')

    def keys(self):
        return self._wo_dict.keys()

    def values(self):
        return self._wo_dict.values()

    def items(self):
        return self._wo_dict.items()

    def update(self, *args, **kwargs):
        self._wo_dict.update(*args, **kwargs)

    def update_open_wo(self, wo_number, labor_time, parts_cost):
        time_now = time.localtime()
        date_today = time.strftime('%d %m %Y', time_now)
        self._wo_dict[wo_number][6] = date_today
        self._wo_dict[wo_number][7] += labor_time
        self._wo_dict[wo_number][9] += parts_cost
        self._wo_dict[wo_number][8] = self._wo_dict[wo_number][7] * rate
        self._wo_dict[wo_number][10] = self._wo_dict[wo_number][8] + self._wo_dict[wo_number][9]

        return None

    def closing_wo(self, wo_number):
        print(f'comanda inchisa:\n - {wo_number} : {self._wo_dict[wo_number]}')
        reg, vin, brand, model, client, d_in, d_out, labor_t, labor_c, parts_c, total_c = self._wo_dict[wo_number]
        wo_closing = WorkOrder(reg, vin, brand, model, client, d_in, d_out, labor_t, parts_c, wo_number)
        del (self._wo_dict[wo_number])

        return wo_closing


class WorkOrdersClosed(WorkOrdersDict):

    def __init__(self, *args):
        super().__init__(*args)

    def __setitem__(self, key, item):
        raise TypeError ('WorkOrdersClosed unmutable object')

    def __delitem__(self, key):
        raise TypeError('WorkOrdersClosed unmutable object')


def move_wo(wo_number_move, labor_time_move, parts_cost_move):
    work_orders_dict.update_open_wo(wo_number_move, labor_time_move, parts_cost_move)
    wo_closed = work_orders_dict.closing_wo(wo_number_move)
    work_orders_closed.update(WorkOrdersClosed(wo_closed))


def close_wo(wo_number_close=None, labor_time_close=None, parts_cost_close=None):
    if wo_number_close and labor_time_close and parts_cost_close:
        move_wo(wo_number_close, labor_time_close, parts_cost_close)
    else:
        wo_number_close = input('introdu numarul comenzii pe care doresti sa o inchizi : ')
        labor_time_close = float(input(f'introdu orele de manopera aferente comenzii {wo_number_close} : '))
        parts_cost_close = float(input(f'introdu costul pieselor aferente comenzii {wo_number_close} : '))
        move_wo(wo_number_close, labor_time_close, parts_cost_close)


def header_prep():
    items = (
        ('work order no.', 14), ('reg.no.', 9), ('vin', 19), ('brand', 15), ('model', 15), ('client', 19),
        ('date_in', 13), ('date_out', 13), ('labot_time', 12), ('parts_cost', 12), ('labor_cost', 12),
        ('total_cost', 12)
    )
    header = ''
    for title, lenght in items:
        item = title.center(lenght)
        header = ' '.join((header, item))
    return header


def print_open_wo():
    time_now = time.localtime()
    date_today = time.strftime('%d %m %Y', time_now)
    open_wo_counter = len(work_orders_dict)
    print(f'\nIn data de {date_today} sunt {open_wo_counter} comenzi deschise:\n')
    print(header_prep())
    print(work_orders_dict)


def print_closed_wo():
    print(f'\nComenzi inchise:\n')
    print(header_prep())
    print(work_orders_closed)


# print open or close work orders by input(car or client)
def print_oc_wo_by_input(input_data, car_client, open_close):
    if car_client == 'car' and open_close == 'open':
        wo_by_input, _ = work_orders_dict.work_orders_by_input(input_data, car_client)
        state = 0

    elif car_client == 'car' and open_close == 'close':
        wo_by_input, list_of_data = work_orders_closed.work_orders_by_input(input_data, car_client)
        state = 1

    elif car_client == 'client' and open_close == 'open':
        wo_by_input, _ = work_orders_dict.work_orders_by_input(input_data, car_client)
        state = 2

    elif car_client == 'client' and open_close == 'close':
        wo_by_input, list_of_data = work_orders_closed.work_orders_by_input(input_data, car_client)
        state = 3

    else:
        raise ValueError('Date incorecte')

    counter = len(wo_by_input)
    condition = car_client == 'car'
    condition_2 = counter == 1
    text = ['comanda deschisa', 'comanda inchisa', 'comenzi deschise', 'comenzi inchise']

    print_data = f'\n{"Automobilul cu numarul" if condition else "Clientul"} {input_data} are {counter} ' \
                 f'{text[state]}:\n{header_prep()}\n{wo_by_input}'

    if state == 1 or state == 3:
        print_closed_data = f'{"Automobilul cu numarul" if condition else "Clientul"} {input_data} a acumulat ' \
                            f'{counter} factur{"a" if condition_2 else "i"}:\n' \
                            f'- ore de manopera:         {list_of_data[0]:,} h\n' \
                            f'- valoare manopera:        {list_of_data[2]:,} ron\n' \
                            f'- valoare piese de schimb: {list_of_data[1]:,} ron\n' \
                            f'- valoare totatala:        {list_of_data[3]:,} ron\n'
    else:
        print_closed_data = ''

    print_final_data = f'{"*" * 30}\n{print_data}\n{print_closed_data}\n{"*" * 30}'
    print(print_final_data)


#from autoworkshop import *

# preparing data

rate = 100
work_orders_dict = WorkOrdersDict()
work_orders_closed = WorkOrdersClosed()
time_now = time.localtime()
date_today = time.strftime('%d %m %Y', time_now)

car_1 = WorkOrder('cj20hap', 'vf225478541235478', 'peugeot', '206 hdi', 'sc parcauto sa', '03 05 2020')
work_orders_dict.update(WorkOrdersDict(car_1))
car_2 = WorkOrder('cj55adb', 'vf125478541235478', 'renault', 'clio 1.5dci', 'sc pfa sa', '07 05 2020')
work_orders_dict.update(WorkOrdersDict(car_2))
car_3 = WorkOrder('B100eee', 'wba25478541235478', 'bmw', '335 xi', 'sc parcauto sa', '08 05 2020')
work_orders_dict.update(WorkOrdersDict(car_3))
car_4 = WorkOrder('B100eee', 'wdb25478598745214', 'mercedes', 'C 220 cdi', 'sc pfa sa')
work_orders_dict.update(WorkOrdersDict(car_4))
car_5 = WorkOrder('cj20ooo', 'vf325422541235478', 'citroen', 'c3 hdi', 'sc pfa sa')
work_orders_dict.update(WorkOrdersDict(car_5))
car_6 = WorkOrder('mm15ury', 'uu125478541235478', 'dacia', '1310', 'Nicolae Mosut')
work_orders_dict.update(WorkOrdersDict(car_6))
car_7 = WorkOrder('mm15ury', 'uu125478541235478', 'dacia', '1310', 'Nicolae Mosut')
work_orders_dict.update(WorkOrdersDict(car_7))
car_8 = WorkOrder('cj45ole', 'wob25478541457846', 'opel', 'antara', 'Gicu pop')
work_orders_dict.update(WorkOrdersDict(car_8))
car_9 = WorkOrder('mm15ury', 'uu125478541235478', 'dacia', '1310', 'Nicolae Mosut')
work_orders_dict.update(WorkOrdersDict(car_9))
car_10 = WorkOrder('mm15ury', 'uu125478541235478', 'dacia', '1310', 'Nicolae Mosut')
work_orders_dict.update(WorkOrdersDict(car_10))

print_open_wo() # check

list_for_closing = [
    ['200503001', 60, 1500],
    ['200507002', 110, 20000],
    ['200508003', 3, 800],
    ['200511004', 2.5,600],
    ['200511006', 30, 8000],
    ['200511007', 12, 4500],
    ['200511010', 17, 5500]
]

for a, b, c in list_for_closing:
    print(f'{a} - {b} - {c}')
    close_wo(a, b, c)

close_wo('200511008', 4, 850)
print_open_wo()
print_closed_wo()

print_oc_wo_by_input('mm15ury', 'car', 'open')
print_oc_wo_by_input('sc pfa sa', 'client', 'open')
print_oc_wo_by_input('B100eee', 'car', 'close')
print_oc_wo_by_input('mm15ury', 'car', 'close')
print_oc_wo_by_input('Nicolae Mosut', 'client', 'close')

del (work_orders_closed['200511010'])
