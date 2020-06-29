from application import Garage, Reports, Truck, FixedValues, UpdatedValues, Report

fixed_values = FixedValues(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
initial_updated_values = UpdatedValues(0, "", 0, "", 0, "", 0, "")
second_updated_values = UpdatedValues(1, "", 2, "tire break", 1, "", 1, "")

garage = Garage()
reports = Reports()

plate_number = "CJ01RAR"
truck: Truck = Truck(plate_number, True)

if not garage.is_truck_defined(plate_number):
    garage.add_element(truck)
    if garage.__getitem__(plate_number) is not None:
        print('Truck added in garage with success')
    else:
        print('[1] Should not be here in ELSE')
else:
    print('[2] Should not be here in ELSE')

if garage.is_truck_defined(plate_number):
    print("Truck with " + plate_number + " it is stored in garage")
else:
    print('[3] Should not be here in ELSE')

if garage.truck_availability(plate_number) and garage.__len__() == 1:
    print("Truck is available in garage")
else:
    print('[4] Should not be here in ELSE')

garage.send_truck_on_road(plate_number)
first_report = Report(fixed_values, initial_updated_values)
reports[plate_number] = [first_report]

if not garage.truck_availability(plate_number):
    print('Truck is on the road')
else:
    print('[5] Should not be here in ELSE')

if reports.__getitem__(plate_number) is not None:
    print('Report added with success')
else:
    print('[6] Should not be here in ELSE')

if garage.is_truck_defined(plate_number):
    print('Cannot add another truck with the same plate number')
else:
    print('[7] Should not be here in ELSE')

print('Sending a new report')
new_report = Report(fixed_values, second_updated_values) + first_report
reports_list = reports.__getitem__(plate_number)
reports_list.append(new_report)

if len(reports_list) == 2:
    print('There are two reports for truck ' + plate_number)
    print("The first one when the truck was sent on road")
    print("And the second one when the a week updated was given")

print("Printing now the 2 reports")
reports_sequence = reports.set_reports_sequence(plate_number)
try:
    current_report: Report = next(reports_sequence)
    while current_report is not None:
        current_report.calculate_for_report()
        current_report: Report = next(reports_sequence)
except StopIteration:
    pass


truck1: Truck = Truck('CJ02PYT', True)
truck2: Truck = Truck('CJ01PYT', True)