

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
class Automobil(object):
    clasa = 'automobil'

    def __init__(self, marca, tip, varianta, an, cilindree, putere):
        self.marca = marca
        self.tip = tip
        self.var = varianta
        self.an = an
        self.cil = int(cilindree)
        self.putere = int(putere)

# method that converts the power from [kW] in [hp] and compare it wit a specific value
    def test_putere(self):
        if int(self.putere * 1.36) >= 200:
            print(f'\nAutomobilul {self.marca} {self.var} din {self.an} dezvolta',
                  f'{int(self.putere * 1.36)} cai putere, automobil sportiv.')
        else:
            print(f'\nAutomobilul {self.marca} {self.var} din {self.an} dezvolta',
                  f'{int(self.putere * 1.36)} cai putere, are putere medie.')

# method that print a message
    @staticmethod
    def print_step():
        print('\nTEST DE PUTERE')

# method that calculate the taxes for a vahicle
    def impozit(self):
        for x in range(len(test_cilindree) - 1):
            if self.cil in range(test_cilindree[x], test_cilindree[x + 1]):
                print(f'\nPentru automobilul {self.marca} {self.var} a carui motor',
                      f'are cilindreea de {self.cil} cmc, impozitul anual este',
                      f'{calculator_impozit(self.cil, x):.2f} lei')
        if self.cil >= 3001:
            print(f'\nPentru automobilul {self.marca} {self.var} a carui motor',
                  f'are cilindreea de {self.cil} cmc, impozitul anual este',
                  f'{calculator_impozit(self.cil, x + 1):.2f} lei')

# child class of Automobil class an ads some new proprieties
class ConsumCombustibil(Automobil):

    def __init__(self, marca, tip, varianta, an, cilindree, putere, consum_mediu):
        self.consum = float(consum_mediu)
        super().__init__(marca, tip, varianta, an, cilindree, putere)

# methode calculates how many km cand you do with the fuel from the tank
    def autonomie(self):
        cantitate = float(input('\nIntrodu cantitatea de combustibil din rezervor [l]: '))
        auton = cantitate / self.consum * 100
        print(f'\nCu {cantitate} litri de combustibil poti parcurge {auton:.0f} km.')
        input('\n\33[31mPress Enter to continue...\033[0m')

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} {} - {} {} {}) [{}]'.format(
            class_name, self.marca,
            self.tip, self.var, self.an, self.cil, self.putere, id(self)
        )

    def __str__(self):
        return '{} {} {} - {} {} {}'.format(
            self.marca.ljust(10, ' '),
            self.tip.ljust(10, ' '), self.var.ljust(8, ' '), self.an,
            str(self.cil).center(10), str(self.putere).center(8))

class ParcAuto():

    def __init__(self, auto_list=None):
        self._autos = list(auto_list) if auto_list else []

    def __iter__(self):
        return iter(self._autos)

# function calculate the auto txes
def calculator_impozit(cil, indice):
    return cil / 200 * indice_impozit[indice]

# function for inputing the vhicle datas
def auto_input():
    return ConsumCombustibil(
        input('Introdu marca automobilului:'),
        input('Introdu tipul automobilului: '),
        input('Introdu varianta automobilului: '),
        input('introdu anul de fabricatie: '),
        input('Introdu cilindreea motorului [cmc]: '),
        input('Introdu puterea motorului [kw]:'),
        input('Introdu consumul mediu de combustibil [l/100km]:')
    )

# function process auto datas
def prelucrare_parcauto(lista):
    for auto in lista:
        auto.impozit()
        auto.print_step()
        auto.test_putere()
        auto.autonomie()


indice_impozit = (8, 19, 76, 153, 308)
test_cilindree = (0, 1601, 2001, 2601, 3001)

# creates the list with vehicles
automobil_list = [
    ConsumCombustibil('BMW', 'Seria 5', '530d', 2015, 2996, 210, 9.6),
    ConsumCombustibil('Audi', 'A4', '2.0Tdi', 2012, 1946, 140, 6.3),
    ConsumCombustibil('Mercedes', 'C-classe', 'C220cdi', 2014, 2156, 150, 7.4)
]

parc_auto = ParcAuto(automobil_list)

print('\nse vor prelucra datele pentru urmatoaarea lista de automobile: \n')
print('\n  MARCA      TIP    VARIANTA      AN   CILINDREE  PUTERE')

# print the list with vehicles
for auto in parc_auto:
    print(auto)

input('\n\33[31mPress Enter to continue...\033[0m')

prelucrare_parcauto(parc_auto)

auto1 = auto_input()
auto1.print_step()
auto1.test_putere()
auto1.impozit()
auto1.autonomie()
