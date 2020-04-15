

'''
Build two classes of your choice that can model a real-life example.
The class needs to meet the following requirements:

    at least 5 attributes each

    at least 2 methods each

    one class to inherit from another

As a demonstration create at least 5 instances of
one class (preferably the child class) and
call all the methods it holds

Ex: You can have one class (Country) that has general attributes
about countries such as area, neighbours, cities etc and
methods related to those attributes. The second class can be a
specific country (Romania) that has more specific attributes
such as attractions, universities etc.
'''

# main class (parent class)
class Car(object):
    category = 'automobil'

    def __init__(self, brand, series, version, year, cubic_cap, power):
        self.brand = brand
        self.series = series
        self.var = version
        self.year = year
        self.cub_c = int(cubic_cap)
        self.power = int(power)

    # method that converts the power from [kW] in [hp] and compare it wit a specific value
    def print_message_medium_high_power(self):
        if int(self.power * 1.36) >= 200:
            print(
                f'\nAutomobilul {self.brand} {self.var} din {self.year} dezvolta',
                f'{int(self.power * 1.36)} cai putere, automobil sportiv.'
            )
        else:
            print(
                f'\nAutomobilul {self.brand} {self.var} din {self.year} dezvolta',
                f'{int(self.power * 1.36)} cai putere, are putere medie.'
            )

    # method that print a message
    @staticmethod
    def print_step():
        print('\nTEST DE PUTERE')

    # method that calculate the taxes for a vahicle
    def tax(self):
        cubic_cil_test = (0, 1601, 2001, 2601, 3001)
        for x in range(len(cubic_cil_test) - 1):
            if self.cub_c in range(cubic_cil_test[x], cubic_cil_test[x + 1]):
                print(f'\nPentru automobilul {self.brand} {self.var} a carui motor',
                      f'are cilindreea de {self.cub_c} cmc, impozitul anual este',
                      f'{tax_calc(self.cub_c, x):.2f} lei')
        if self.cub_c >= 3001:
            print(f'\nPentru automobilul {self.brand} {self.var} a carui motor',
                  f'are cilindreea de {self.cub_c} cmc, impozitul anual este',
                  f'{tax_calc(self.cub_c, x + 1):.2f} lei')

# child class of Automobil class an ads some new proprieties
class FuelCons(Car):

    def __init__(self, brand, series, version, year, cubic_cap, power, med_cons):
        self.cons = float(med_cons)
        super().__init__(brand, series, version, year, cubic_cap, power)

    # method calculates how many km cand you do with the fuel from the tank
    def range(self):
        quantity = float(input('\nIntrodu cantitatea de combustibil din rezervor [l]: '))
        range_var = quantity / self.cons * 100
        print(f'\nCu {quantity} litri de combustibil poti parcurge {range_var:.0f} km.')
        input('\n\33[31mPress Enter to continue...\033[0m')

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} {} - {} {} {}) [{}]'.format(
            class_name, self.brand,
            self.series, self.var, self.year, self.cub_c, self.power, id(self)
        )

    def __str__(self):
        return '{} {} {} - {} {} {}'.format(
            self.brand.ljust(10, ' '),
            self.series.ljust(10, ' '), self.var.ljust(8, ' '), self.year,
            str(self.cub_c).center(10), str(self.power).center(8))

class AutoFleet():

    def __init__(self, auto_list=None):
        self._autos = list(auto_list) if auto_list else []

    def __iter__(self):
        return iter(self._autos)
    

# function calculate the auto txes
def tax_calc(cub_c, ind):
    return cub_c / 200 * tax_ind[ind]

# function for inputing the vhicle datas
def auto_input():
    return FuelCons(
        input('Introdu marca automobilului:'),
        input('Introdu tipul automobilului: '),
        input('Introdu varianta automobilului: '),
        input('introdu anul de fabricatie: '),
        input('Introdu cilindreea motorului [cmc]: '),
        input('Introdu puterea motorului [kw]:'),
        input('Introdu consumul mediu de combustibil [l/100km]:')
    )

# function process auto datas
def fleet_processing(list_in):
    for auto in list_in:
        auto.tax()
        auto.print_step()
        auto.print_message_medium_high_power()
        auto.range()


tax_ind = (8, 19, 76, 153, 308)


# creates the list with vehicles
cars_list = [
    FuelCons('BMW', 'Seria 5', '530d', 2015, 2996, 210, 9.6),
    FuelCons('Audi', 'A6', '2.0Tdi', 2012, 1960, 140, 6.3),
    FuelCons('Mercedes', 'C-classe', 'C220cdi', 2014, 2156, 150, 7.4)
]

auto_fleet = AutoFleet(cars_list)


print('\nse vor prelucra datele pentru urmatoaarea lista de automobile: \n')
print('\n  MARCA      TIP    VARIANTA      AN   CILINDREE  PUTERE')

# print the list with vehicles
for auto in auto_fleet:
    print(auto)

input('\n\33[31mPress Enter to continue...\033[0m')

fleet_processing(auto_fleet)

auto1 = auto_input()
auto1.print_step()
auto1.print_message_medium_high_power()
auto1.tax()
auto1.range()
