"""
# Lesson 14 - Operator Overloading

## Challenge:

Design a class Challenge!

Create a Challenge similar to the ones we included in previous lessons. The challenge must touch the following points:
>      1. Try to present a real example inspired by your work or passions
>
>      2. Require operator overloading to solve at least one requirement of the challenge
>
>      3. At least one bonus, optional requirement
>

The challenge must contain any extra pieces of information that are required for completing the challenge such as definition, logic diagrams, etc. The challenge will be written in the markdown format and saved in a .md file

Attach the solution of the challenge

"""
import time


class WorkOrder: # Mechanical Work Order

    def __init__(self, registation, vin, brand, model, client, date_in=None, date_out=None, labor=0.0, parts_cost=0.0, number=None):

        counter_wo_number = str(len(work_orders_dict) + len(work_orders_closed) + 1).rjust(3, '0')
        now = time.localtime()
        now_2 = time.strftime('%d %m %Y', now)

        if labor == 0 and not date_in:
            self.wo_number = f'{now_2[8: 10]}{now_2[3: 5]}{now_2[0: 2]}{counter_wo_number}'
            self.date_in = now_2
        elif labor == 0 and date_in :
            self.date_in = date_in
            self.wo_number = f'{date_in[8: 10]}{date_in[3: 5]}{date_in[0: 2]}{counter_wo_number}'
        else:
            self.wo_number = number
            self.date_in = date_in


        self.registration = registation
        self.vin = vin
        self.brand = brand
        self.model = model
        self.client = client

        # if date_in == None:
        #     self.date_in = now_2
        # else:
        #     self.date_in = date_in

        if date_out == None:
            self.date_out = date_out
        else:
            self.date_out = now_2

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
        return (f'{self.wo_number} : {self.registration}, {self.vin}, {self.brand}, {self.model}, '
               f'{self.client}, {self.date_in}, {date_out_print}, {self.labor:.2f} h, {self.parts_cost:.2f} ron, '
               f'{self.labor_cost:.2f} ron, {self.total_cost:.2f} ron')

    def __iter__(self):
        return iter(self._list_of_data)

    def __len__(self):
        return len(self._list_of_data)

    def __getitem__(self, item):
        return self._list_of_data[item]

    def __contains__(self, item):
        return item in self._list_of_data


class WorkOrdersDict(dict):

    def __init__(self, item_in=None):
        self._wo_dict = {}
        if item_in:
            self.key = item_in[0]
            self.value = item_in[1:len(item_in)]
            self._wo_dict = {self.key: self.value}

    def __str__(self):
        # date_in_print = time.strftime('%d %m %Y', self.value[5])
        # if self.date_out is None:
        #     date_out_print = 'open'
        ordered_keys_list = list(self._wo_dict.keys())
        ordered_keys_list.sort()
        print_dict = ''
        for print_iter in ordered_keys_list:
            print_dict += ''.join(f' - {print_iter} : {[value for value in self._wo_dict[print_iter]]}\n') # {print_iter}, {self.vin}, {self.brand}, {self.model}, '
              #  f'{self.client}, {date_in_print[0: 10]}, {date_out_print}, {self.labor:.2f} h, {self.parts_cost:.2f} ron, '
               # f'{self.labor_cost:.2f} ron, {self.total_cost:.2f} ron\n').upper().join()
        return print_dict

    # def __str__(self):
    #     return f'ooo{self._wo_dict}'

    def __iter__(self):
        return iter(self._wo_dict)

    def __len__(self):
        return  len(self._wo_dict)

    def __setitem__(self, key, item):
        self._wo_dict[key] = item

    def __getitem__(self, key):
        return self._wo_dict[key]

    def __delitem__(self, key):
        del self._wo_dict[key]

    def keys(self):
        return self._wo_dict.keys()

    def values(self):
        return self._wo_dict.values()

    def items(self):
        return self._wo_dict.items()

    def update(self, *args, **kwargs):
        self._wo_dict.update(*args)

    def close_wo(self, wo_dict , wo_number, labor_time, parts_cost):
        now = time.localtime()
        now_2 = time.strftime('%d %m %Y', now)

        wo_dict[wo_number][6] = now_2
        wo_dict[wo_number][7] = labor_time
        wo_dict[wo_number][9] = parts_cost
        wo_dict[wo_number][8] = wo_dict[wo_number][7] * rate
        wo_dict[wo_number][10] = wo_dict[wo_number][8] + wo_dict[wo_number][9]
        reg, vin, brand, model, client, d_in, d_out, labor_t, labor_c, parts_c, total_c = wo_dict[wo_number]
        auto_closed = WorkOrder(reg, vin, brand, model, client, d_in, d_out, labor_t, parts_c, wo_number)

        print(f'comanda inchisa:\n - {wo_number} : {wo_dict[wo_number]}')

        return auto_closed

class WorkOrdersClosed(WorkOrdersDict):

    def __init__(self, *args):
        super().__init__(*args)
        #print('mmm', self._wo_dict)

    # def __init__(self, item_in):
    #     self.key = item_in[0]
    #     self.value = item_in[1:len(item_in)]
    #     self._wo_dict = {self.key: self.value}
    #     print('kkk', self._wo_dict)
    #
    #
    # def update(self, *args, **kwargs):
    #     print('kkk', self._wo_dict)
    #     self._wo_dict.update(*args)

# preparing data
rate = 100
work_orders_dict = WorkOrdersDict()
work_orders_closed = WorkOrdersClosed()


car_0 = WorkOrder('cj20ooo', 'vf325422541235478', 'citroen', 'c3 hdi', 'sc pfa sa', '03 05 2020', None, 0, 0)
work_orders_dict.update(WorkOrdersDict(car_0))
car_1 = WorkOrder('cj20hap', 'vf225478541235478', 'peugeot', '206 hdi', 'sc parcauto sa', None, None, 0, 0)
work_orders_dict.update(WorkOrdersDict(car_1))
car_2 = WorkOrder('cj55adb', 'vf125478541235478', 'renault', 'clio 1.5dci', 'sc abc srl', None, None, 0, 0)
work_orders_dict.update(WorkOrdersDict(car_2))
car_3 = WorkOrder('B100eee', 'wba25478541235478', 'bmw', '335 xi', 'sc parcauto sa', None, None, 0, 0)
work_orders_dict.update(WorkOrdersDict(car_3))
car_4 = WorkOrder('cj20hap', 'vf225478541235478', 'peugeot', '206 hdi', 'Sorin Mosut', None, None, 0, 0)
work_orders_dict.update(WorkOrdersDict(car_4))

# check
print(work_orders_dict)


def close_wo(wo_number_close = None, labor_time_close = None , parts_cost_close = None):
    check = 'y'
    while check == 'y':
        if wo_number_close and labor_time_close and parts_cost_close:
            auto_closed = work_orders_dict.close_wo(work_orders_dict, wo_number_close, labor_time_close, parts_cost_close)
            work_orders_closed.update(WorkOrdersClosed(auto_closed))
            del work_orders_dict[auto_closed[0]]
            check = input('doresti sa inchizi o comanda de lucru [y/n] : ')
        else:
            wo_number_close = input('introdu numarul comenzii pe care doresti sa o inchizi : ')
            labor_time_close = float(input(f'introdu orele de manopera aferente comenzii {wo_number_close} : '))
            parts_cost_close = float(input(f'introdu costul pieselor aferente comenzii {wo_number_close} : '))

            auto_closed = work_orders_dict.close_wo(work_orders_dict, wo_number_close, labor_time_close,
                                                    parts_cost_close)
            work_orders_closed.update(WorkOrdersClosed(auto_closed))
            del work_orders_dict[auto_closed[0]]
            wo_number_close = None
            labor_time_close = None
            parts_cost_close = None
            check = input('doresti sa inchizi o comanda de lucru [y/n] : ')

def print_open_wo():
    now = time.localtime()
    now_2 = time.strftime('%d %m %Y', now)
    open_wo_counter = len(work_orders_dict)
    print(f'\nIn data de {now_2} sunt {open_wo_counter} comenzi deschise :\n\n{work_orders_dict}')

def print_closed_wo():
    print(f'\ncomenzi inchise : \n')
    print(work_orders_closed)


close_wo()
print_open_wo()
print_closed_wo()



car_5 = WorkOrder('mm15ury', 'uu125478541235478', 'dacia', '1310', 'Nicolae Mosut', None, None, 0, 0)
work_orders_dict.update(WorkOrdersDict(car_5))
print_open_wo()

close_wo('200507006', 6, 1350)
print_open_wo()
print_closed_wo()


# for key in work_orders_dict:
#      print(f'{key} : {work_orders_dict[key]}')



