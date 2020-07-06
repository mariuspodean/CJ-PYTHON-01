from final_project.edmond_sabou.application import *
import unittest
import random
rand_cnp = "".join(random.choices(string.digits, k=13))


class TestClientPackagesContracts(unittest.TestCase):

    def test_package(self):
        package = TouristicPackage(99, "Sejur Grecia", "Sejur Greacia in luna Septembrie", 650)
        assert package.index == 99
        assert package.title == "Sejur Grecia"
        assert package.description == "Sejur Greacia in luna Septembrie"
        assert package.price == 650

        package.description = "Sejur ANULAT!!"
        package.title = "Sejur Grecia - ANULAT!"
        package.price = 1
        assert package.title == "Sejur Grecia - ANULAT!"
        assert package.description == "Sejur ANULAT!!"
        assert package.price == 1

    def test_package_validator_empty_index(self):
        package = TouristicPackage("", "This ia a test", "Ana are mere", 999)
        validate = package.validate()
        try:
            if validate:
                assert False
        except ValueError:
            assert True

    def test_package_validator_with_empty_fields(self):
        package = TouristicPackage(1, "", "", 123)
        validate = package.validate()
        try:
            if validate:
                assert False
        except ValueError:
            assert True

    def test_package_validator_with_float_value(self):
        package = TouristicPackage(2, "This ia a test", "Ana are mere", 99.9)
        validate = package.validate()
        try:
            if validate:
                assert False
        except ValueError:
            assert True

    def test_package_validator_with_negative_value(self):
        package = TouristicPackage(2, "This ia a test", "Ana are mere", -999)
        validate = package.validate()
        try:
            validate
        except ValueError:
            assert True

    def test_client_class(self):
        client = Client(1, 'Edi', 'Sabou', '1234567890123')
        assert client.index == 1
        assert client.name == 'Edi'
        assert client.surname == 'Sabou'
        assert client.cnp == '1234567890123'
        client.name = 'Sam'
        client.surname = 'Pilgrim'
        client.cnp = client.cnp
        assert client.index == 1
        assert client.name == 'Sam'
        assert client.surname == 'Pilgrim'

    def test_contract_class(self):
        contract = Contract(1, 2, "Sejur Grecia", '1234567890123')
        assert contract.id_package == 2
        assert contract.cnp == '1234567890123'

        contract.cnp = '0987654321098'
        contract.id_contract = 3
        assert contract.id_package == 2
        assert contract.cnp == '0987654321098'

    def test_contract_validator(self):
        contract = Contract(1, 3, "Contract", '2233445566771')
        validate = contract.validate()
        try:
            if validate:
                assert True
        except ValueError:
            assert False

    def test_contract_with_empty_string(self):
        contract = Contract("", "", "", "")
        validate = contract.validate()
        try:
            validate()
            assert False
        except ValueError:
            assert True

    def test_contract_with_less_than_13_cnp(self):
        contract = Contract(1, 3, "Contract", '223344556')
        validate = contract.validate()
        try:
            validate()
            assert False
        except ValueError:
            assert True

    def test_contract_with_more_than_13_cnp(self):
        contract = Contract(1, 3, "Contract", '223344556223344556223344556')
        validate = contract.validate()
        try:
            validate()
            assert False
        except ValueError:
            assert True

    def test_store_client(self):
        client = Client("1", 'QWE', 'ZXC', "1234567890456")
        file = ClientsHandler("../test_clients.txt")
        file.store_client(client)
        try:
            file.find_client(client)
            assert True
        except ValueError:
            assert False

    def test_remove_client(self):
        client = Client(55, 'rtyui', 'kjhg', '0004599990123')
        file = ClientsHandler("../test_clients.txt")
        file.store_client(client)
        file.remove_client("0004599990123")
        try:
            file.find_client("0004599990123")
            assert True
        except ValueError:
            assert False

    def test_store_contract(self):
        contract = Contract(4, 2, "Olala", "1234567890123")
        file = ContractsFileHandler("../FINAL_PROJ/test_contracts.txt")
        file.store_contract(contract)
        try:
            if file.size_contract() == "1":
                assert True
        except ValueError:
            assert False

    def test_remove_contract(self):
        contract = Contract(1, 2, "ABC", '1234567440123'"")
        file = ContractsFileHandler("../FINAL_PROJ/test_contracts.txt")
        file.store_contract(contract)
        assert file.size_contract() == 1
        file.remove_contract(1)
        assert file.size_contract() == 0

if __name__ == "__main__":
    unittest.main()
