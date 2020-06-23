# unit converter
type_of_unit_list = ['pressure', 'force', 'temperature']
pressure_list = ['psi', 'bar', 'N/mm2']
force_list = ['N', 'lbf']
temperature_list = ['°C', '°F']

from_unit_temp_list = []
to_unit_temp_list = []

type_of_unit = ''

from_unit = ''

to_unit = ''

requested_value = ''


class Pressure(object):
    def __init__(self, unit_variable):
        self.unit_variable = unit_variable

    def pressure_convert(self):
        if from_unit == 'psi' and to_unit == 'bar':
            return f'{requested_value} [psi] is {round((self.unit_variable * 0.0689475729), 2)} [bar]'

        elif from_unit == 'bar' and to_unit == 'psi':
            return f'{requested_value} [bar] is {round((self.unit_variable * 14.503773773), 2)} [psi]'

        elif from_unit == 'bar' and to_unit == 'N/mm2':
            return f'{requested_value} [bar] is {round((self.unit_variable * 0.1), 2)} [N/mm2]'

        elif from_unit == 'N/mm2' and to_unit == 'bar':
            return f'{requested_value} [N/mm2] is  {round((self.unit_variable * 10), 2)} [bar]'

        elif from_unit == 'psi' and to_unit == 'N/mm2':
            return f'{requested_value} [psi] is  {round((self.unit_variable * 0.00689475728), 2)} [N/mm2]'

        elif from_unit == 'N/mm2' and to_unit == 'psi':
            return f'{requested_value} [N/mm2] is  {round((self.unit_variable * 14.503773773), 2)} [psi]'


class Force(object):
    def __init__(self, unit_variable):
        self.unit_variable = unit_variable

    def force_convert(self):
        if from_unit == 'N' and to_unit == 'lbf':
            return f'{requested_value} [N] is {round((self.unit_variable * 0.22480894387096), 2)} [lbf]'

        elif from_unit == 'lbf' and to_unit == 'N':
            return f'{requested_value} [N] is {round((self.unit_variable * 4.4482216), 2)} [N]'


class Temperature(object):
    def __init__(self, unit_variable):
        self.unit_variable = unit_variable

    def temperature_convert(self):
        if from_unit == 'C' and to_unit == 'F':
            return f'{requested_value} [°C] is {round(((self.unit_variable * (9 / 5)) + 32), 2)} [°F]'

        elif from_unit == 'F' and to_unit == 'C':
            return f'{requested_value} [°F] is {round(((1 - self.unit_variable) * (5 / 9)), 2)} [°C]'


class AllToKilometers:
    def __init__(self, kilometers, miles):
        self.kilometers = kilometers
        self.miles = miles

    def __add__(self, other):
        total_km = self.kilometers + other.kilometers
        total_miles_to_km = (self.miles * 1.60934) + (other.miles * 1.60934)
        total = total_km + total_miles_to_km
        return total


#  ************      user interaction   *****************************************************
def question_type_of_unit():
    print('What type of unit do you want to convert?')
    for index, item in enumerate(type_of_unit_list, start=1):
        print(f'{index}: {item}')


def question_from_unit():
    print('From which unit do you want to convert?')
    for index, item in enumerate(from_unit_temp_list, start=1):
        print(f'{index}: {item}')


def question_to_unit():
    print('To which unit do you want to convert?')
    for index, item in enumerate(to_unit_temp_list, start=1):
        print(f'{index}: {item}')


def main():
    global from_unit_temp_list, to_unit_temp_list, type_of_unit, from_unit, to_unit, requested_value
    # type of unit
    question_type_of_unit()
    question_type_input = int(input())
    if question_type_input == 1:  # pressure related procedures
        type_of_unit = 'pressure'
        from_unit_temp_list = pressure_list
        question_from_unit()
        question_from_unit_input = int(input())
        if question_from_unit_input == 1:
            from_unit = 'psi'
            pressure_list.remove('psi')
            to_unit_temp_list = pressure_list
            question_to_unit()
            question_to_unit_input = int(input())
            if question_to_unit_input == 1:
                to_unit = 'bar'
                print('Please enter value to transform: ')
                requested_value = int(input())
            if question_to_unit_input == 2:
                to_unit = 'N/mm2'
                print('Please enter value to transform: ')
                requested_value = int(input())
        if question_from_unit_input == 2:
            from_unit = 'bar'
            pressure_list.remove('bar')
            to_unit_temp_list = pressure_list
            question_to_unit()
            question_to_unit_input = int(input())
            if question_to_unit_input == 1:
                to_unit = 'psi'
                print('Please enter value to transform: ')
                requested_value = int(input())
            if question_to_unit_input == 2:
                to_unit = 'N/mm2'
                print('Please enter value to transform: ')
                requested_value = int(input())
        if question_from_unit_input == 3:
            from_unit = 'N/mm2'
            pressure_list.remove('N/mm2')
            to_unit_temp_list = pressure_list
            question_to_unit()
            question_to_unit_input = int(input())
            if question_to_unit_input == 1:
                to_unit = 'psi'
                print('Please enter value to transform: ')
                requested_value = int(input())
            if question_to_unit_input == 2:
                to_unit = 'bar'
                print('Please enter value to transform: ')
                requested_value = int(input())
    if question_type_input == 2:  # force related procedures
        type_of_unit = 'force'
        from_unit_temp_list = force_list
        question_from_unit()
        question_from_unit_input = int(input())
        if question_from_unit_input == 1:
            from_unit = 'N'
            to_unit = 'lbf'
            print('Please enter value to transform: ')
            requested_value = int(input())
        if question_from_unit_input == 2:
            from_unit = 'lbf'
            to_unit = 'N'
            print('Please enter value to transform: ')
            requested_value = int(input())
    if question_type_input == 3:  # temperature related procedures
        type_of_unit = 'temperature'
        from_unit_temp_list = temperature_list
        question_from_unit()
        question_from_unit_input = int(input())
        if question_from_unit_input == 1:
            from_unit = 'C'
            to_unit = 'F'
            print('Please enter value to transform: ')
            requested_value = int(input())
        if question_from_unit_input == 2:
            from_unit = 'F'
            to_unit = 'C'
            print('Please enter value to transform: ')
            requested_value = int(input())


main()


#  ************      user interaction   ****************************************************

#  ************      results   ******************
def box_it(fnc):
    def inner_func():
        print("*" * 20)
        fnc()
        print("*" * 20)

    return inner_func


@box_it
def results():
    if type_of_unit == 'pressure':
        result = Pressure(requested_value)
        print(result.pressure_convert())
    elif type_of_unit == 'force':
        result = Force(requested_value)
        print(result.force_convert())
    elif type_of_unit == 'temperature':
        result = Temperature(requested_value)
        print(result.temperature_convert())


results()


# for overloading
@box_it
def to_overloading():
    distance1 = AllToKilometers(10, 5)
    distance2 = AllToKilometers(15, 20)

    distance_overall = distance1 + distance2

    print(f' {round(distance_overall, 2)} km')


to_overloading()

#  ************      results   ******************
