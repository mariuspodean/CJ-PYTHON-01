from final_project.mosut_sorin.basic_data import build_car_client_instance, Car, CarsDataBase, save_instance, Client, \
    ClientsDataBase
# from final_project.mosut_sorin.main_data import*
import unittest


class TestData(unittest.TestCase):

    def test_cars_class_has_proper_atributes(self):
        # arange
        vin = 'VF1JSH72459495489'
        reg_no = 'B587EEE'
        brand = 'Dacia'
        model = 'Logan'
        cill = 1180
        power = 65
        year = 2014
        # act
        test_cars = CarsDataBase()
        car_object = build_car_client_instance(Car, vin, reg_no, brand, model, cill, power, year, data_base=test_cars)
        save_instance(car_object, test_cars)
        # assert
        assert car_object[0] == vin and \
               test_cars['VF1JSH72459495489'][0] == reg_no and \
               test_cars['VF1JSH72459495489'][1] == brand and \
               test_cars['VF1JSH72459495489'][2] == model and \
               test_cars['VF1JSH72459495489'][3] == cill and \
               test_cars['VF1JSH72459495489'][4] == power and \
               test_cars['VF1JSH72459495489'][5] == year and \
               vin in test_cars.keys(), 'incorect Car object atributes'

    def test_clients_class_has_proper_atributes(self):
        # arange
        client_id = 'RO778554'
        name = 'SC Python SA'
        adress = 'Cluj-Napoca Bdul 22 Decembrie 1989 164/9'
        # act
        test_clients = ClientsDataBase()
        client_object = build_car_client_instance(Client, client_id, name, adress, data_base=test_clients)
        save_instance(client_object, test_clients)
        # assert
        assert client_object[0] == client_id and test_clients['RO778554'][0] == name and \
               test_clients['RO778554'][1] == adress and \
               client_id in test_clients.keys(), 'incorect Car object atributes'


if __name__ == '__main__':
    unittest.main()
