import unittest

from application import PlateNumber, Truck, Garage, FixedValues, UpdatedValues, Report, Reports

plate_nr = "CJ22PYT"
new_plate_nr = "CJ33PYT"


class TestPlateNumber(unittest.TestCase):

    def test_get_plate_number(self):
        pn = PlateNumber(plate_nr)
        self.assertEqual(pn.plate_number, plate_nr)

    def test_set_plate_number(self):
        pn = PlateNumber(plate_nr)
        self.assertEqual(pn.plate_number, plate_nr)

        pn.plate_number = new_plate_nr
        self.assertEqual(pn.plate_number, new_plate_nr)


class TestTruck(unittest.TestCase):

    def test_get_plate_number(self):
        truck = Truck(plate_nr, True)
        self.assertEqual(truck.plate_number, plate_nr)

    def test_set_plate_number(self):
        truck = Truck(plate_nr, True)
        self.assertEqual(truck.plate_number, plate_nr)

        truck.plate_number = new_plate_nr
        self.assertEqual(truck.plate_number, new_plate_nr)


class TestGarage(unittest.TestCase):

    def test_garage_init(self):
        garage = Garage()

        self.assertEqual(garage.__len__(), 0)

    def test_add_element(self):
        garage = Garage()
        truck = Truck(plate_nr, True)
        garage.add_element(truck)

        self.assertEqual(garage.__len__(), 1)

    def test_send_truck_on_road(self):
        garage = Garage()
        truck = Truck(plate_nr, True)
        garage.add_element(truck)
        truck_from_garage = garage.__getitem__(plate_nr)

        self.assertEqual(truck_from_garage.available, True)
        self.assertEqual(truck_from_garage.plate_number, plate_nr)

        garage.send_truck_on_road(plate_nr)
        self.assertEqual(garage.__len__(), 1)

        update_truck = garage.__getitem__(plate_nr)
        self.assertEqual(update_truck.available, False)


class TestFixedValues(unittest.TestCase):

    def test_get_leasing(self):
        leasing = 1
        fixed_values = FixedValues(leasing, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

        self.assertEqual(fixed_values.leasing, leasing)

    def test_set_leasing(self):
        leasing = 1
        fixed_values = FixedValues(leasing, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        fixed_values.leasing = 11

        self.assertEqual(fixed_values.leasing, 11)

    def test_get_salary(self):
        salary = 2
        fixed_values = FixedValues(1, salary, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

        self.assertEqual(fixed_values.salary, salary)


class TestUpdateValues(unittest.TestCase):
    def test_get_diesel(self):
        diesel = 9
        updated_values = UpdatedValues(diesel, "", 3, "", 5, "", 7, "")

        self.assertEqual(updated_values.updated_diesel, 9)

    def test_set_diesel(self):
        diesel = 9
        updated_values = UpdatedValues(diesel, "", 3, "", 5, "", 7, "")
        updated_values.updated_diesel = 99

        self.assertEqual(updated_values.updated_diesel, 99)


class TestReport(unittest.TestCase):

    def test_get_leasing(self):
        leasing = 1
        fixed_values = FixedValues(leasing, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        updated_values = UpdatedValues(1, "", 3, "", 5, "", 7, "")
        report = Report(fixed_values, updated_values)

        self.assertEqual(report.fixed_values.leasing, 1)

    def test_set_leasing(self):
        leasing = 1
        fixed_values = FixedValues(leasing, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        updated_values = UpdatedValues(1, "", 3, "", 5, "", 7, "")
        report = Report(fixed_values, updated_values)
        report.fixed_values.leasing = 11

        self.assertEqual(report.fixed_values.leasing, 11)


class TestReports(unittest.TestCase):

    def test_insert_report(self):
        garage = Garage()
        truck = Truck(plate_nr, False)
        garage.add_element(truck)
        fixed_values = FixedValues(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        updated_values = UpdatedValues(1, "", 3, "", 5, "", 7, "")
        report = Report(fixed_values, updated_values)
        reports = Reports()

        reports[plate_nr] = [report]

        self.assertEqual(reports.__getitem__(plate_nr)[0], report)


    def test_del_item(self):
        garage = Garage()
        truck = Truck(plate_nr, False)
        garage.add_element(truck)
        fixed_values = FixedValues(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        updated_values = UpdatedValues(1, "", 3, "", 5, "", 7, "")
        report = Report(fixed_values, updated_values)
        reports = Reports()

        reports.__setitem__(plate_nr, [report])
        reports_list_for_truck = reports.__getitem__(plate_nr)
        self.assertEqual(reports_list_for_truck[0], report)

        reports.__delitem__(plate_nr)
        self.assertEqual(None, reports.__getitem__(plate_nr))


if __name__ == '__main__':
    unittest.main()