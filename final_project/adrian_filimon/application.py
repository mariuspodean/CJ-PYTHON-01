import os
import sys


class Calculator:
    def compute_difference(self, a, b):
        return a - b

    def compute_sum(self, a, b):
        return a + b

    def compute_multiplication(self, a, b):
        return a * b


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def __str__(self):
        return "FileManager(filename=" + self.filename + "mode=" + self.mode + ")"

    def __repr__(self):
        return {'filename': self.filename, 'mode': self.mode}


class PlateNumber:
    def __init__(self, pn):
        self.plate_number = pn

    @property
    def plate_number(self):
        return self.__plate_number

    @plate_number.setter
    def plate_number(self, pn):
        self.__plate_number = pn

    def __str__(self):
        return "PlateNumber(plateNumber=" + self.plate_number + ")"

    def __repr__(self):
        class_name = type(self).__name__
        return f' {type(self.plate_number)}, {class_name}'


class Truck(PlateNumber):
    def __init__(self, plate_number: str, available: bool):
        PlateNumber.__init__(self, plate_number)
        self.__available = available

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, a):
        self.__available = a

    def __str__(self):
        return "Truck(plateNumber=" + self.plate_number + ", available=" + str(self.available) + ")"

    def __repr__(self):
        class_name = id(self.plate_number)
        return f' {type(self.plate_number)}, {class_name}'


class Garage(Calculator):
    def __init__(self):
        self.trucks = []

    @property
    def trucks(self):
        return self.__trucks

    @trucks.setter
    def trucks(self, g):
        self.__trucks = g

    def add_element(self, truck):
        self.trucks = self.compute_sum(self.trucks, [truck])

    def send_truck_on_road(self, plate_number):
        truck: Truck
        for truck in self.trucks:
            if truck.plate_number == plate_number:
                truck.available = False
                break

    def truck_availability(self, plate_number):
        truck: Truck = self.__getitem__(plate_number)
        if truck is not None:
            return truck.available
        return False

    def is_truck_defined(self, plate_number):
        truck: Truck = self.__getitem__(plate_number)
        if truck is not None and truck.plate_number == plate_number:
            return True
        return False

    def __getitem__(self, plate_number):
        truck: Truck
        for truck in self.trucks:
            if truck.plate_number == plate_number:
                return truck
        return None

    def __len__(self):
        return len(self.trucks)

    def __contains__(self, plate_number):
        truck: Truck
        for truck in self.trucks:
            if truck.plate_number == plate_number:
                return True
        return False

    def __str__(self):
        trucks = "Garage cars: \n"
        for truck in self.trucks:
            status = "In garage"
            if not truck.available:
                status = 'On road'
            trucks += "\t" + truck.plate_number + " - " + status + "\n"

        return trucks

    def __repr__(self):
        trucks = "\tGarage cars: \n"
        for truck in self.trucks:
            status = "In garage"
            if not truck.available:
                status = 'On road'
            trucks += "\t" + truck.plate_number + " - " + status + "\n"

        return trucks


class FixedValues(Calculator):
    def __init__(self, leasing: float, salary: float, insurance: float, office_salary: float, eurovignete: float,
                 bonus_driver: float, km_price: float, km_extra_price: float, diesel: float, other_costs: float,
                 days_on_road: int, km: float):
        self.leasing = leasing
        self.salary = salary
        self.insurance = insurance
        self.office_salary = office_salary
        self.eurovignete = eurovignete
        self.bonus_driver = bonus_driver
        self.km_price = km_price
        self.km_extra_price = km_extra_price
        self.diesel = diesel
        self.other_costs = other_costs
        self.days_on_road = days_on_road
        self.kilometers = km

    @property
    def leasing(self):
        return self.__leasing

    @leasing.setter
    def leasing(self, l):
        self.__leasing = l

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        self.__salary = s

    @property
    def insurance(self):
        return self.__insurance

    @insurance.setter
    def insurance(self, i):
        self.__insurance = i

    @property
    def office_salary(self):
        return self.__office_salary

    @office_salary.setter
    def office_salary(self, os):
        self.__office_salary = os

    @property
    def eurovignete(self):
        return self.__eurovignete

    @eurovignete.setter
    def eurovignete(self, e):
        self.__eurovignete = e

    @property
    def bonus_driver(self):
        return self.__bonus_driver

    @bonus_driver.setter
    def bonus_driver(self, bd):
        self.__bonus_driver = bd

    @property
    def km_price(self):
        return self.__km_price

    @km_price.setter
    def km_price(self, kp):
        self.__km_price = kp

    @property
    def km_extra_price(self):
        return self.__km_extra_price

    @km_extra_price.setter
    def km_extra_price(self, km_ep):
        self.__km_extra_price = km_ep

    @property
    def diesel(self):
        return self.__diesel

    @diesel.setter
    def diesel(self, d):
        self.__diesel = d

    @property
    def other_costs(self):
        return self.__other_costs

    @other_costs.setter
    def other_costs(self, oc):
        self.__other_costs = oc

    @property
    def days_on_road(self):
        return self.__days_on_road

    @days_on_road.setter
    def days_on_road(self, dor):
        self.__days_on_road = dor

    @property
    def kilometers(self):
        return self.__kilometers

    @kilometers.setter
    def kilometers(self, k):
        self.__kilometers = k

    def amount_for_kilometers_done(self):
        return self.compute_multiplication(self.km_price, self.kilometers)

    def expected_payed_amount(self):
        return self.leasing + self.salary + self.insurance + self.office_salary + self.eurovignete + self.bonus_driver

    def __str__(self) -> str:
        return "FixedValues=(leasing=" + str(self.leasing) + "salary=" + str(self.salary) + "insurance=" + \
               str(self.insurance) + "officeSalary=" + str(self.office_salary) + "eurovignete=" + str(
            self.eurovignete) + \
               "bonusDriver=" + str(self.bonus_driver) + "kmPrice=" + str(self.km_price) + "kmExtraPrice=" + \
               str(self.km_extra_price) + "diesel=" + str(self.diesel) + "otherCosts=" + str(self.__other_costs) + \
               "daysOnRoad=" + str(self.days_on_road) + "kilometers=" + str(self.kilometers) + ")"

    def __repr__(self):
        return {
            'leasing': str(self.leasing),
            'salary': str(self.salary),
            'insurance': str(self.insurance),
            'officeSalary': str(self.office_salary),
            'eurovignete': str(self.eurovignete),
            'bonusDriver': str(self.bonus_driver),
            'kmPrice': str(self.km_price),
            'kmExtraPrice': str(self.km_extra_price),
            'diesel': str(self.diesel),
            'otherCosts': str(self.other_costs),
            'daysOnRoad': str(self.days_on_road),
            'kilometers': str(self.kilometers),
        }


class UpdatedValues:
    def __init__(self, diesel, diesel_details, other_costs, other_costs_details, days_on_road, days_on_road_details, km,
                 km_details):
        self.updated_diesel = diesel
        self.updated_other_costs = other_costs
        self.updated_days_on_road = days_on_road
        self.updated_kilometers = km

        self.diesel_details = diesel_details
        self.other_costs_details = other_costs_details
        self.days_on_road_details = days_on_road_details
        self.kilometers_details = km_details

    @property
    def updated_diesel(self):
        return self.__updated_diesel

    @updated_diesel.setter
    def updated_diesel(self, d):
        self.__updated_diesel = d

    @property
    def updated_other_costs(self):
        return self.__updated_other_costs

    @updated_other_costs.setter
    def updated_other_costs(self, oc):
        self.__updated_other_costs = oc

    @property
    def updated_days_on_road(self):
        return self.__updated_days_on_road

    @updated_days_on_road.setter
    def updated_days_on_road(self, dor):
        self.__updated_days_on_road = dor

    @property
    def updated_kilometers(self):
        return self.__updated_kilometers

    @updated_kilometers.setter
    def updated_kilometers(self, k):
        self.__updated_kilometers = k

    @property
    def diesel_details(self):
        return self.__diesel_details

    @diesel_details.setter
    def diesel_details(self, d):
        self.__diesel_details = d

    @property
    def other_costs_details(self):
        return self.__other_costs_details

    @other_costs_details.setter
    def other_costs_details(self, oc):
        self.__other_costs_details = oc

    @property
    def days_on_road_details(self):
        return self.__days_on_road_details

    @days_on_road_details.setter
    def days_on_road_details(self, dor):
        self.__days_on_road_details = dor

    @property
    def kilometers_details(self):
        return self.__kilometers_details

    @kilometers_details.setter
    def kilometers_details(self, k):
        self.__kilometers_details = k

    def __str__(self):
        return "UpdatedValue=(diesel=" + str(self.updated_diesel) + "dieselDetails=" + str(self.diesel_details) + \
               "otherCosts=" + str(self.updated_other_costs) + "otherCostsDetails=" + str(self.other_costs_details) + \
               "daysOnRoad=" + str(self.updated_days_on_road) + "daysOnRoadDetails=" + str(self.days_on_road_details) + \
               "kilometers=" + str(self.__updated_kilometers) + "kilometersDetails=" + str(
            self.kilometers_details) + ")"

    def __repr__(self):
        return {
            'diesel': str(self.updated_diesel),
            'dieselDetails': str(self.diesel_details),
            'otherCosts': str(self.updated_other_costs),
            'otherCostsDetails': str(self.other_costs_details),
            'daysOnRoad': str(self.updated_other_costs),
            'daysOnRoadDetails': str(self.days_on_road_details),
            'kilometers': str(self.updated_kilometers),
            'kilometersDetails': str(self.kilometers_details)
        }


class Report(Calculator):
    def __init__(self, fixed_values: FixedValues, updated_values: UpdatedValues):
        self.fixed_values = fixed_values
        self.updated_values = updated_values

    @property
    def fixed_values(self):
        return self.__fixed_values

    @fixed_values.setter
    def fixed_values(self, fv):
        self.__fixed_values = fv

    @property
    def updated_values(self):
        return self.__updated_values

    @updated_values.setter
    def updated_values(self, uv):
        self.__updated_values = uv

    def calculate_for_report(self):
        fixed_values: FixedValues = self.fixed_values
        updated_values: UpdatedValues = self.updated_values
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\tExpected leasing: " + str(fixed_values.leasing))
        print("\tExpected salary: " + str(fixed_values.salary))
        print("\tExpected insurance: " + str(fixed_values.insurance))
        print("\tExpected office salary: " + str(fixed_values.office_salary))
        print("\tExpected eurovignete: " + str(fixed_values.eurovignete))
        print("\tExpected bonus driver: " + str(fixed_values.bonus_driver))
        print("\tPrice/KM: " + str(fixed_values.km_price))
        print("\tExtra price/KM: " + str(fixed_values.km_extra_price))
        print('=========================================================')
        print("\t\t\tProfit/Loss: " + str(-fixed_values.expected_payed_amount()))
        print("---------------------------------------------------------")
        print('\tExpected diesel: ' + str(fixed_values.diesel))
        print('\tActual diesel : ' + str(updated_values.updated_diesel))
        print('\tDiesel details: ' + str(updated_values.diesel_details))

        print('\tExpected other costs: ' + str(fixed_values.other_costs))
        print('\tActual other costs : ' + str(updated_values.updated_other_costs))
        print('\tOther costs details: ' + str(updated_values.other_costs_details))

        print('\tExpected days: ' + str(fixed_values.days_on_road))
        print('\tActual days on road : ' + str(updated_values.updated_days_on_road))
        print('\tDays on road details: ' + str(updated_values.days_on_road_details))

        print('\tExpected KM: ' + str(fixed_values.kilometers))
        print('\tActual KM: ' + str(updated_values.updated_kilometers))
        print('\tKM details: ' + str(updated_values.kilometers_details))

        diesel_costs = self.compute_difference(fixed_values.diesel, updated_values.updated_diesel)
        amount_for_other_costs = self.compute_difference(fixed_values.other_costs, updated_values.updated_other_costs)
        kilometers_done = self.compute_difference(fixed_values.kilometers, updated_values.updated_kilometers)

        total_profit_loss = -fixed_values.expected_payed_amount() + amount_for_other_costs + diesel_costs

        print("---------------------------------------------------------")
        if kilometers_done < 0:
            amount_for_expected_km = self.fixed_values.amount_for_kilometers_done()
            amount_for_extra_km = self.compute_multiplication(-kilometers_done, fixed_values.km_extra_price)
            total_profit_loss += self.compute_sum(amount_for_extra_km, amount_for_expected_km)
            print("\tPrice for KM done: " + str(amount_for_expected_km))
            print("\tExtra KM done: " + str(-kilometers_done))
            print("\tPayed for extra KM done: " + str(amount_for_extra_km))
        else:
            amount_for_real_kilometers = self.compute_multiplication(fixed_values.km_price,
                                                                     updated_values.updated_kilometers)
            total_profit_loss += amount_for_real_kilometers
            print("\tPrice for KM done: " + str(amount_for_real_kilometers))
        print('=========================================================')
        print("\t\t\tTOTAL Profit/Loss: " + str(total_profit_loss))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    def __add__(self, other: 'Report'):
        new_diesel = self.compute_sum(self.updated_values.updated_diesel, other.updated_values.updated_diesel)
        other_costs = self.compute_sum(self.updated_values.updated_other_costs,
                                       other.updated_values.updated_other_costs)
        no_of_days = self.compute_sum(self.updated_values.updated_days_on_road,
                                      other.updated_values.updated_days_on_road)
        target = self.compute_sum(self.updated_values.updated_kilometers, other.updated_values.updated_kilometers)

        diesel_details_output = self.updated_values.diesel_details
        if other.updated_values.diesel_details != "":
            diesel_details_output += self.compute_sum(" - ", other.updated_values.diesel_details)

        other_costs_details_output = self.updated_values.other_costs_details
        if other.updated_values.other_costs_details != "":
            other_costs_details_output += self.compute_sum(" - ", other.updated_values.other_costs_details)

        no_of_days_details_output = self.updated_values.days_on_road_details
        if other.updated_values.days_on_road_details != "":
            no_of_days_details_output += self.compute_sum(" - ", other.updated_values.days_on_road_details)

        target_details_output = self.updated_values.kilometers_details
        if other.updated_values.kilometers_details != "":
            target_details_output += self.compute_sum(" - ", other.updated_values.kilometers_details)

        self.updated_values.updated_diesel = new_diesel
        self.updated_values.updated_other_costs = other_costs
        self.updated_values.updated_days_on_road = no_of_days
        self.updated_values.updated_kilometers = target

        self.updated_values.diesel_details = diesel_details_output
        self.updated_values.other_costs_details = other_costs_details_output
        self.updated_values.days_on_road_details = no_of_days_details_output
        self.updated_values.kilometersDetails = target_details_output

        return self

    def __str__(self) -> str:
        return "Report(FixedValues(" + self.fixed_values + "), UpdatedValues(" + self.updated_values + ")"

    def __repr__(self):
        return {'fixedValues': self.fixed_values, 'updatedValues': self.updated_values}


class Reports(Calculator):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)

    def set_reports_sequence(self, plate_number: str):
        for pn in self.__dict__:
            if pn == plate_number:
                truck_reports = self.__dict__[pn]
                for report in truck_reports:
                    yield report
                break

    def need_new_fixed_file(self, plate_number: str):
        for pn in self.__dict__:
            if pn == plate_number:
                truck_reports = self.__dict__[pn]
                if len(truck_reports) != 0 and len(truck_reports) % 5 == 0:
                    return True
        return False

    def get_pos_for_wanted_fixed_value_file(self, plate_number: str):
        for pn in self.__dict__:
            if pn == plate_number:
                truck_reports = self.__dict__[pn]
                if len(truck_reports) != 0:
                    integer_part = len(truck_reports) // 5
                    return self.compute_multiplication(integer_part, 5)

    def __setitem__(self, key: str, value):
        self.__dict__[key] = value

    def __getitem__(self, key: str):
        try:
            return self.__dict__[key]
        except KeyError:
            return None

    def __delitem__(self, key: str):
        try:
            del self.__dict__[key]
        except KeyError:
            return None

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __str__(self):
        pretty_print = ""
        for key, value in self.__dict__.items():
            pretty_print += key + " - " + ", ".join(value)
        return pretty_print

    def __repr__(self):
        return '{}, D({})'.format(super(Reports, self).__repr__(), self.__dict__)


def read_fixed_values():
    try:
        print('\tPlease input the fixed data:')
        leasing = float(input("\t\tLeasing: "))
        salary = float(input("\t\tSalary: "))
        insurance = float(input("\t\tInsurance: "))
        office_salary = float(input("\t\tOffice salary: "))
        eurovignete = float(input("\t\tEurovignete: "))
        bonus_driver = float(input("\t\tBonus driver: "))
        km_price = float(input("\t\tPrice/KM: "))
        km_extra_price = float(input("\t\tExtra price/KM: "))
        diesel = float(input("\t\tDiesel: "))
        other_costs = float(input("\t\tOther costs: "))
        days_on_road = int(input("\t\tDays on road: "))
        kilometers = float(input("\t\tKilometers: "))

        return FixedValues(leasing, salary, insurance, office_salary, eurovignete, bonus_driver, km_price,
                           km_extra_price,
                           diesel, other_costs, days_on_road, kilometers)
    except:
        print('Something went wrong when reading fixed values...')


def read_week_updated_values():
    try:
        print('\tPlease input the target data:')
        diesel_actual = float(input("\tDiesel: "))
        diesel_details = str(input("\tDiesel details: "))
        other_costs_actual = float(input("\tOther costs: "))
        other_costs_details = str(input("\tOther costs details: "))
        no_of_days_actual = int(input("\tNo. of days: "))
        no_of_days_details = str(input("\tNo. of days details: "))
        target_actual = float(input("\tKilometers: "))
        target_details = str(input("\tKilometers details: "))

        return UpdatedValues(diesel_actual, diesel_details,
                             other_costs_actual, other_costs_details,
                             no_of_days_actual, no_of_days_details,
                             target_actual, target_details)
    except:
        print('Something went wrong when reading updated values...')


def menu_decorator(fnc):
    def inner_func():
        print("\n")
        print("#"*13)
        print("Final Project")
        print("WELCOME TO ~PLANNING AND BUGETTING~")
        print("Adrian Filimon - CJ 01 PYTHON - Scoala Informala Cluj")
        fnc()
        print("Adrian Filimon - CJ 01 PYTHON - Scoala Informala Cluj")
        print("A TRADEMARK OF TRUCKING DEPARTMENT&CO ")
        print("Final Project")
        print("#"*13)
        print("\n")

    return inner_func


@menu_decorator
def print_menu():
    print('\n-------------------------')
    print("1. Add truck")
    print("2. Show trucks")
    print("3. Send truck on road")
    print("4. Truck status report")
    print("5. Reports")
    print("0. Exit\n")
    print('\n-------------------------')


def main():
    file_name = 'garage.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
    garage = Garage()
    reports = Reports()

    while True:
        print_menu()
        try:
            option = int(input("Option: "))
            if option == 0:
                if os.path.exists(file_name):
                    os.remove(file_name)
                sys.exit(0)
            if option == 1:
                plate_number = str(input("\tPlate number: "))
                truck: Truck = Truck(plate_number, True)
                if not garage.is_truck_defined(plate_number):
                    garage.add_element(truck)
                    file_manager = FileManager(file_name, 'w')
                    with file_manager as f:
                        f.write(garage.__repr__())
                else:
                    print('\tTruck already exists.')
            if option == 2:
                if garage.__len__() == 0:
                    print("\tThere are no trucks available")
                else:
                    print()
                    print(garage.__str__())

            if option == 3:
                plate_number = str(input("\tPlate number: "))
                if garage.is_truck_defined(plate_number) and garage.truck_availability(plate_number):
                    garage.send_truck_on_road(plate_number)
                    fixed_values: FixedValues = read_fixed_values()
                    updated_values = UpdatedValues(0, "", 0, "", 0, "", 0, "")
                    report = Report(fixed_values, updated_values)
                    reports[plate_number] = [report]
                    print("\tTruck sent on road")
                else:
                    print('\tTruck does not exist or it is already on road')

            if option == 4:
                plate_number = str(input("\tPlate number: "))
                if garage.is_truck_defined(plate_number):
                    if not reports.need_new_fixed_file(plate_number):
                        updated_values: UpdatedValues = read_week_updated_values()
                        reports_list = reports.__getitem__(plate_number)
                        first_report: Report = reports_list[reports.get_pos_for_wanted_fixed_value_file(plate_number)]
                        last_report: Report = reports_list[len(reports_list) - 1]
                        new_report = Report(first_report.fixed_values, updated_values) + last_report
                        reports_list.append(new_report)
                        reports[plate_number] = reports_list
                    else:
                        print("\tIt's a new month. You need to reed new fixed values, then submit a new report")
                        fixed_values: FixedValues = read_fixed_values()
                        updated_values = UpdatedValues(0, "", 0, "", 0, "", 0, "")
                        report = Report(fixed_values, updated_values)
                        reports_list = reports.__getitem__(plate_number)
                        reports_list.append(report)
                        reports[plate_number] = reports_list
                else:
                    print('\tTruck does not exist')

            if option == 5:
                plate_number = str(input("\tPlate number: "))
                if garage.is_truck_defined(plate_number):
                    reports_sequence = reports.set_reports_sequence(plate_number)
                    try:
                        current_report: Report = next(reports_sequence)
                        while current_report is not None:
                            current_report.calculate_for_report()
                            current_report: Report = next(reports_sequence)
                    except StopIteration:
                        continue
                else:
                    print('\tTruck does not exist or it is already on road')
        except ValueError:
            print('Something went wrong...')


if __name__ == '__main__':
    main()