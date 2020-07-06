import string
import time
import random


class CheckerClientClass:
    def __init__(self, index, name, surname, cnp):
        self.cnp = cnp
        self.surname = surname
        self.name = name
        self.index = index

    def validate(self):

        error_msg = ""
        if self.index is None:
            error_msg += "Id can not be empty "
        if self.name is None:
            error_msg += "Name can not be empty "
        if self.surname is None:
            error_msg += "Surname can not be empty "
        if self.cnp is None:
            error_msg += "CNP can not be empty "
        if len(self.cnp) < 13:
            error_msg += "CNP can not have less than 13 digits "
        if len(self.cnp) > 13:
            error_msg += "CNP can not have more than 13 digits "
        if type(self.cnp) == float:
            error_msg += "CNP can not be float "
        if len(error_msg) > 0:
            raise ValueError(error_msg)
        return True


class Client(CheckerClientClass):

    def __init__(self, index, name, surname, cnp):
        self.index = index
        self.name = name
        self.surname = surname
        self.cnp = cnp
        CheckerClientClass.__init__(self, index, name, surname, cnp)

    def __eq__(self, o: 'Client') -> bool:
        if self.index == o.index or self.cnp == o.cnp:
            return True
        return False

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, new_index):
        self.__index = new_index

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, new_cnp):
        self.__cnp = new_cnp

    def __str__(self):
        return f"ID: {str(self.index)}, Name: {str(self.name)}, Surname: {str(self.surname)}, CNP: {str(self.cnp)}"


class CheckerContractClass:
    def __init__(self, id_contract, id_package, title, cnp):
        self.cnp = cnp
        self.if_contract = id_contract
        self.title = title
        self.id_package = id_package

    def validate(self):

        error_msg = ""
        if self.title is None:
            error_msg += "Package title cannot be empty"
        if self.id_package is None:
            error_msg += "Id cannot be empty;"
        if self.cnp is None:
            error_msg += "cnp cannot be empty"
        if len(self.cnp) < 13:
            error_msg += "cnp cannot have less than 13 digits"
        if len(self.cnp) > 13:
            error_msg += "cnp cannot have more than 13 digits"
        if type(self.cnp) == float:
            error_msg += "cnp cannot be float"
        if not self.cnp.isdigit():
            error_msg += "cnp has to have 13 digits"
        if len(error_msg) > 0:
            raise ValueError(error_msg)
        return True


class Contract(CheckerContractClass):

    def __init__(self, id_contract, id_package, title, cnp):
        self.id_contract = id_contract
        self.id_package = id_package
        self.title = title
        self.cnp = cnp
        CheckerContractClass.__init__(self, id_contract, id_package, title, cnp)

    def __eq__(self, o: 'Contract') -> bool:
        if self.id_contract == o.id_contract or self.id_package == o.id_contract:
            return True
        return False

    @property
    def id_contract(self):
        return self.__id_contract

    @id_contract.setter
    def id_contract(self, new_id):
        self.__id_contract = new_id

    @property
    def id_package(self):
        return self.__id_package

    @id_package.setter
    def id_package(self, new_id_package):
        self.__id_package = new_id_package

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, new_cnp):
        self.__cnp = new_cnp

    def __str__(self):
        return f"Contract ID: {self.id_contract}, Package ID: {self.id_package}, Title: {self.title}, CNP: {self.cnp}"


class CheckerPackageClass:
    def __init__(self, index, title, description, price):
        self.title = title
        self.description = description
        self.price = price
        self.index = index

    def validate(self):

        error_msg = ""
        if self.index is None:
            error_msg += "Id cannot be empty"
        if self.title is None:
            error_msg += "Title cannot be empty"
        if self.price is None:
            error_msg += "Price cannot be empty"
        if int(self.price) < 0:
            error_msg += "Price cannot be negative"
        if type(self.price) == float:
            error_msg += "Year cannot be float"
        if len(error_msg) > 0:
            raise ValueError(error_msg)
        return True


class TouristicPackage(CheckerPackageClass):

    def __init__(self, index, title, description, price):
        self.index = index
        self.title = title
        self.description = description
        self.price = price
        CheckerPackageClass.__init__(self, index, title, description, price)

    def __eq__(self, o: 'TouristicPackage') -> bool:
        if self.index == o.index or self.price == o.price:
            return True
        return False

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, new_index):
        self.__index = new_index

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    def __str__(self):
        return f"ID: {str(self.index)}, Title: {str(self.title)}, Description: {str(self.description)}, " \
               f"Price: {str(self.price)}\n"


class PackageFileContextManager:

    def __init__(self, file_name):
        self._file_name = file_name

    def __enter__(self):
        return open(self._file_name, "r")

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


class PackageFileHandler(PackageFileContextManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def load_from_file(self):
        try:
            with PackageFileContextManager(self._file_name) as file_content:
                read = file_content
        except IOError as e:
            return f"Oops! No such file. {e}"

        line = read.readline().strip()
        result = []

        while line != "":
            attribute = line.split(",")
            package = TouristicPackage(attribute[0], attribute[1], attribute[2], attribute[3])
            result.append(package)
            line = read.readline().strip()
        read.close()
        return result

    def save_to_file(self, list):
        with open(self._file_name, "w") as f:
            for package in list:
                formated_str = f"{str(package.index)},{package.title},{package.description},{str(package.price)}\n"
                f.write(formated_str)

    def store_package(self, package):
        validator = TouristicPackage.validate(package)
        all_packages = self.load_from_file()
        if validator:
            pak: TouristicPackage
            for i in all_packages:
                if i == package:
                    raise ValueError("Package already exists")
            all_packages.append(package)
            self.save_to_file(all_packages)
        else:
            return validator.validate(package)

    def remove_all_packages(self):
        self.save_to_file([])

    def get_all_packages(self):
        return self.load_from_file()

    def size_packages(self):
        return len(self.load_from_file())

    def remove_package(self, title):
        all_packages = self.load_from_file()
        a = -1
        for i in range(len(all_packages)):
            if all_packages[i].title == str(title):
                a = i
        if a == -1:
            raise ValueError(f"No package with title:{title}")
        package = all_packages[a]
        del all_packages[a]
        self.save_to_file(all_packages)
        print(f"Package with Title: {title} is now removed.")
        return package


class ContractsFileContextManager:
    """Context Manager for ClientsHandler Class"""

    def __init__(self, file_name):
        self._file_name = file_name

    def __enter__(self):
        return open(self._file_name, "r")

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


class ContractsFileHandler(ContractsFileContextManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def load_from_file(self):
        try:
            with ContractsFileContextManager(self._file_name) as file_content:
                read = file_content
        except IOError:
            return

        line = read.readline().strip()
        stripped = []

        while line != "":
            attribute = line.split(",")
            client = Contract(attribute[0], attribute[1], attribute[2], attribute[3])
            stripped.append(client)
            line = read.readline().strip()
        read.close()
        return stripped

    def save_to_file(self, list):
        with open(self._file_name, "w") as f:
            for text in list:
                formated_str = f"{str(text.id_contract)},{str(text.id_package)},{text.title},{str(text.cnp)}\n"
                f.write(formated_str)

    def store_contract(self, contract):
        """
          Store thecnpclient client to the file.Overwrite store
          Post: client is stored to the file
        """
        validate = Contract.validate(contract)
        all_contracts = self.load_from_file()
        if validate:
            con: Contract
            for i in all_contracts:
                if i == contract:
                    raise ValueError("Client already exists")
                elif i.id_contract == contract.id_contract:
                    raise ValueError("Duplicate no")
                elif i.cnp == contract.cnp:
                    raise ValueError("Client already exists")
            all_contracts.append(contract)
            self.save_to_file(all_contracts)
        else:
            return validate.validate(contract)

    def remove_contract(self, id):
        all_contracts = self.load_from_file()
        a = -1
        for contract in range(len(all_contracts)):
            if all_contracts[contract].id_contract == str(id):
                a = contract
        if a == -1:
            raise ValueError(f"No contract with this ID: {id}")
        contract = all_contracts[a]
        del all_contracts[a]
        self.save_to_file(all_contracts)
        print(f"Contract with ID:{id} is now removed.")
        return contract

    def remove_all(self):
        self.save_to_file([])

    def size_contract(self):
        return len(self.load_from_file())

    def get_all_contracts(self):
        return self.load_from_file()


class ClientFileContextManager:

    def __init__(self, file_name):
        self._file_name = file_name

    def __enter__(self):
        return open(self._file_name, "r")

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


class ClientsHandler(ClientFileContextManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def load_from_file(self):
        try:
            with ClientFileContextManager(self._file_name) as file_content:
                read = file_content
        except IOError as e:
            return f"Oops! No such file. {e}"

        line = read.readline().strip()
        stripped = []

        while line != "":
            attribute = line.split(",")
            client = Client(attribute[0], attribute[1], attribute[2], attribute[3])
            stripped.append(client)
            line = read.readline().strip()
        read.close()
        return stripped

    def save_to_file(self, client_inst):
        with open(self._file_name, "w") as f:
            for text in client_inst:
                formated_str = f"{str(text.index)},{text.name},{text.surname},{str(text.cnp)}\n"
                f.write(formated_str)

    def store_client(self, client):
        validator = Client.validate(client)
        all_clients = self.load_from_file()
        if validator:
            cl: Client
            for cl in all_clients:
                if cl == client:
                    raise ValueError("Duplicate no or CNP")
            all_clients.append(client)
            self.save_to_file(all_clients)
        else:
            return validator.validate(client)

    def remove_client(self, cnp):
        all_clients = self.load_from_file()
        a = -1
        for i in range(len(all_clients)):
            if all_clients[i].cnp == str(cnp):
                a = i
        if a == -1:
            raise ValueError(f"No client with CNP:{cnp}")
        client = all_clients[a]
        del all_clients[a]
        self.save_to_file(all_clients)
        print(f"Client with CNP:{cnp} is now removed.")
        return client

    def find_client(self, cnp):
        clients = self.load_from_file()
        for client in clients:
            if client.cnp == cnp:
                return client
        return None

    def get_all_clients(self):
        return self.load_from_file()

    def size_client(self):
        return len(self.load_from_file())


class ClientTools:
    def __init__(self, file):
        self.file = file
        self.no = 0

    def create_client(self, name, surname, cnp):
        if self.file.get_all_clients():
            empty_list = self.file.get_all_clients()
            list_id = int(empty_list[-1].index)
            self.no = list_id + 1
        else:
            self.no = self.no + 1

        client_id = self.no

        client = Client(client_id, name, surname, cnp)
        validate = client.validate()
        try:
            if validate:
                self.file.store_client(client)
                return True
            else:
                self.no = self.no - 1
                return validate
        except ValueError as error:
            self.no = self.no - 1
            return error

    def random_client_creator(self):
        client_list = []

        rand_id = "".join(random.choices(string.digits, k=4))
        rand_name = "".join(random.choices(string.ascii_letters, k=5))
        rand_surname = "".join(random.choices(string.ascii_letters, k=7))
        rand_cnp = "".join(random.choices(string.digits, k=13))
        client = Client(rand_id, rand_name, rand_surname, rand_cnp)
        if client in client_list:
            print("")
        else:
            client_list.append(client)
            return client

    def search_client(self, cnp):
        """Search for client after name and surname"""
        list = []
        client_list = self.file.get_all_clients()
        for client in client_list:
            if client.cnp == cnp:
                list.append(client)
        if len(list) != 0:
            return list
        else:
            return None

    def show_client(self):
        clients = self.file.get_all_clients()
        if len(clients) > 0:
            for client in clients:
                yield client

    def update_client(self, cnp, new_name, new_surname, new_cnp):
        """Updates an existing client"""
        client_list = self.file.get_all_clients()
        for client in client_list:
            if client.cnp == cnp:
                client.name = new_name
                client.surname = new_surname
                client.cnp = new_cnp
                print(f"\nClient updated to {new_name} {new_surname}, CNP: {new_cnp}")
                self.file.save_to_file(client_list)
                break

    def get_client_cnp(self, cnp):
        client = []
        client_list = self.file.get_all_clients()
        for cl in client_list:
            if cl.cnp == cnp:
                client.append(cl)
            return client

    def print_client_list(self):
        return self.file.get_all_clients()

    def delete_client(self, cnp):
        self.file.remove_client(cnp)
        return self.file


class PackageTools:

    def __init__(self, file):
        self.file = file
        self.no = 0

    def delete_package(self, title):
        self.file.remove_package(title)
        return self.file

    def create_package2(self, title, description, price):
        if self.file.get_all_packages():
            empty_list = self.file.get_all_packages()
            id_list = int(empty_list[-1].index)
            self.no = id_list + 1
        else:
            self.no = self.no + 1

        package_id = self.no
        package = TouristicPackage(package_id, title, description, price)
        validator = package.validate()
        if validator:
            self.file.store_package(package)
            return True
        else:
            self.no = self.no - 1
            return validator.validate(package)

    def show_package_list(self):
        clients = self.file.get_all_packages()
        if len(clients) > 0:
            for client in clients:
                yield client

    def get_all_packages(self):
        return self.file.get_all_packages()

    def search_package_title(self, title):
        empty_list = []

        all_packages = self.file.get_all_packages()
        for package in all_packages:
            if package.title == title:
                empty_list.append(package)
        if len(empty_list) != 0:
            return empty_list
        else:
            return None

    def update_package(self, title, new_title, new_description, new_price):
        package_list = self.file.get_all_packages()
        for pak in package_list:
            if pak.title == title:
                pak.title = new_title
                pak.description = new_description
                pak.price = new_price
                print(f"\nPackage updated to name: {new_title} description: {new_description} and price: {new_price}")
                self.file.save_to_file(package_list)
                break


class ContractTools:

    def __init__(self, file):
        self.file = file
        self.no = 0

    def create_contract(self, id_package, title, cnp):

        if self.file.get_all_contracts():
            empty_list = self.file.get_all_contracts()
            list_id = int(empty_list[-1].id_contract)
            self.no = list_id + 1
        else:
            self.no = self.no + 1

        id = self.no

        contracts_inst = Contract(id, id_package, title, cnp)
        validate = contracts_inst.validate()

        try:
            if validate:
                self.file.store_contract(contracts_inst)
                return True
            else:
                self.no = self.no - 1
                return True
        except ValueError as error:
            self.no = self.no - 1
            return error

    def delete_contract(self, id):
        return self.file.remove_contract(id)

    def get_all_contracts(self):
        return self.file.get_all_contracts()

    def search_contract(self, index):
        empty_list = []

        all_c = self.file.get_all_contracts()
        for c in all_c:
            if c.id_contract == index:
                empty_list.append(c)
        if len(empty_list) != 0:
            return empty_list
        else:
            return None

    def cnp_client(self, contract):
        return contract.cnp()

    def id_package(self, contract):
        return str(contract.id_package())

    def show_contract(self):
        contracts = self.file.get_all_contracts()

        if len(contracts) > 0:
            for contract in contracts:
                yield contract

    def update_contract(self, ind, new_id_package, new_cnp):
        all_contracts_lists = self.file.get_all_contracts()
        for contract in all_contracts_lists:
            if contract.id_contract == ind:
                contract.id_package = new_id_package
                contract.cnp = new_cnp
                self.file.store_contracts(all_contracts_lists)
                break


def make_highlight(func):
    annotations = ["-", "*", "+", "-", ":", "^", "#"]
    annotate = random.choice(annotations)

    def highlight(*args):
        print(annotate * 55)

        func(*args)

        print(annotate * 55)

    return highlight


class UI:

    def __init__(self, client, package, contract):
        self.client = client  # ClientTools(ClientHandler("../ui/clients_file.txt"))
        self.package = package  # PackageTools(PackageHandler("../ui/packages_file.txt"))
        self.contract = contract  # ContractTools(ContractsFileHandler("../ui/contracts_file.txt"))

    def main_menu(self):
        print("Welcome to the UI\n")
        print("1. Clients")
        print("2. Contracts")
        print("3. Packages")
        print("4. Exit")
        return input("Answer: ").strip()

    @make_highlight
    def clients_menu(self):
        print("This is the clients_file Menu, you can do the following:\n")
        print("1. Add client")
        print("2. Search for client")
        print("3. Remove client")
        print("4. Update client")
        print("5. Create random client - DEV ONLY -")
        print("6. Interrogate client list")
        print("7. Back to the Main Menu")

    @make_highlight
    def contract_menu(self):
        print("This is the Contracts Menu, you can do the following:\n")
        print("1. Add contract")
        print("2. Search for contract")
        print("3. Remove contract")
        print("4. Interrogate how many contracts_file you have in the list")
        print("5. Back to the Main Menu")

    @make_highlight
    def packages_menu(self):
        print("This is the Packages Menu, you can do the following:\n")
        print("1. Add package")
        print("2. Search for package")
        print("3. Remove package")
        print("4. Update package")
        print("5. Interrogate package list")
        print("6. Back to the Main Menu")

    ###################

    def begin(self):
        """Launch the app"""
        running = True
        while running is True:
            cmd = self.main_menu()
            if cmd == "4":
                print("\nExiting...")
                time.sleep(1)
                running = False
            if cmd == "1":
                run = True
                self.clients_menu()
                while run is True:
                    answer = input("\nOption:").strip()
                    if answer == "1":
                        self.create_client()
                        answer = "8"
                    if answer == "2":
                        self.search_client()
                        answer = "8"
                    if answer == "3":
                        self.remove_client()
                        answer = "8"
                    if answer == "4":
                        self.update_client()
                    if answer == "5":
                        self.random_client()
                    if answer == "6":
                        self.interrogate_client_list()
                    if answer == "7":
                        run = False

            if cmd == "2":
                run = True
                self.contract_menu()
                while run is True:
                    answer = input("\nOption: ".strip())
                    if answer == "1":
                        self.create_contract()
                    if answer == "2":
                        self.search_contracts()
                    if answer == "3":
                        self.remove_contract()
                    if answer == "4":
                        self.interrogate_contract_list()
                    if answer == "5":
                        run = False

            if cmd == "3":
                run = True
                self.packages_menu()
                while run is True:
                    answer = input("\nOption:").strip()
                    if answer == "1":
                        self.create_package()
                        answer = "8"
                    if answer == "2":
                        self.search_package()
                        answer = "8"
                    if answer == "3":
                        self.remove_package()
                        answer = "8"
                    if answer == "4":
                        self.update_package()
                    if answer == "5":
                        self.interrogate_package_list()
                    if answer == "6":
                        run = False

    @make_highlight
    def interrogate_package_list(self):
        packages = self.package.show_package_list()
        try:
            current_package = next(packages)
            current_displayed = 0
            while current_package is not None:
                if current_displayed > 0 and current_displayed % 5 == 0:
                    self.iteration_menu()
                    it_answer = int(input("\nOption:"))
                    if int(it_answer) == 0:
                        raise StopIteration
                print(current_package)
                current_displayed += 1
                current_package = next(packages)
        except StopIteration:
            print("No more packages to show.")

    @make_highlight
    def interrogate_contract_list(self):
        contracts = self.contract.show_contract()
        try:
            current_contract = next(contracts)
            current_displayed = 0
            while current_contract is not None:
                if current_displayed > 0 and current_displayed % 5 == 0:
                    self.iteration_menu()
                    it_answer = int(input("\nOption:"))
                    if int(it_answer) == 0:
                        raise StopIteration
                print(current_contract)
                current_displayed += 1
                current_contract = next(contracts)
        except StopIteration:
            print("No more contracts to show.")

    @make_highlight
    def interrogate_client_list(self):
        clients = self.client.show_client()
        try:
            current_client = next(clients)
            current_displayed = 0
            while current_client is not None:
                if current_displayed > 0 and current_displayed % 5 == 0:
                    self.iteration_menu()
                    it_answer = int(input("\nOption:"))
                    if int(it_answer) == 0:
                        raise StopIteration
                print(current_client)
                current_displayed += 1
                current_client = next(clients)
        except StopIteration:
            print("No more clients to show.")

    def iteration_menu(self):
        print("\n1. Show more?")
        print("0. Exit")

    @make_highlight
    def show_package(self):
        if self.package.show_package_list():
            print("Package list: ")
            self.package.show_package_list()
        else:
            print("Package list is empty.")
            return None

    @make_highlight
    def create_package(self):
        title = input("Provide the package name: ")
        description = input("Provide the package description: ")
        price = input("Provide the package price: ")

        try:
            package = self.package.create_package2(title, description, price)
            if package is True:
                print(
                    f"\n The package with title {title.upper()} and price: {price} has been added.")
            else:
                print(package)
        except ValueError as e:
            print(e)

    @make_highlight
    def remove_package(self):
        pak_name = input("Provide package name: ")
        self.package.delete_package(pak_name)
        self.package.show_package_list()

    @make_highlight
    def search_package(self):
        print("Search package\n")
        package_title = input("Package title: ")
        if self.package.search_package_title(package_title) is not None:
            for pack in self.package.search_package_title(package_title):
                print(pack)
        else:
            print(f"Package with name: {package_title} has not been found.")

    @make_highlight
    def remove_client(self):
        cnp = int(input("Provide client CNP: "))
        self.client.get_client_cnp(cnp)
        self.client.delete_client(cnp)
        self.client.print_client_list()

    @make_highlight
    def create_client(self):
        name = str(input("Provide the client's name: "))
        surname = str(input("Provide the client's surname: "))
        cnp = input("Type client CNP: ")

        try:
            client = self.client.create_client(name, surname, cnp)
            if client is True:
                ok = True
                if ok is False:
                    print("Cannot create")
                    self.client.remove_client(cnp)
                else:
                    print(f"\nClient with name {name.upper()} {surname.upper()} has been added.\n")
            else:
                print(client)
        except ValueError as error:
            print(f"Duplicate! {error}")

    @make_highlight
    def search_client(self):
        print("\nSearch client\n")
        client_cnp = str(input("Provide the client's CNP: "))
        if self.client.search_client(client_cnp) is not None:
            for client in self.client.search_client(client_cnp):
                print(client)
        else:
            print(f"Client with CNP: {client_cnp} was not found")

    @make_highlight
    def update_client(self):
        print("\nUpdate client\n")
        cnp = str(input("Provide the client's CNP: "))
        if self.client.search_client(cnp) is not None:
            for client in self.client.search_client(cnp):
                print(client)
            new_name = str(input("Provide new client name: "))
            new_surname = str(input("Provide new client surname: "))
            new_cnp = str(input("Provide new client CNP: "))
            self.client.update_client(cnp, new_name, new_surname, new_cnp)
        else:
            print(f"Client was not found")

    @make_highlight
    def update_package(self):
        print("\nUpdate package\n")
        pak_title = str(input("Provide package title: "))
        if self.package.search_package_title(pak_title) is not None:
            for pak in self.package.search_package_title(pak_title):
                print(pak)
            new_title = str(input("Provide new package title: "))
            new_description = str(input("Provide new package description: "))
            new_price = str(input("Provide new package price: "))
            self.package.update_package(pak_title, new_title, new_description, new_price)
        else:
            print("Package was not found")

    @make_highlight
    def create_contract(self):
        package_name = input("Provide package name you wish to buy: ")
        client_cnp = input("Provide client cnp: ")
        if package_name is None or client_cnp is None:
            print("Name or CNP is empty, try again.")
            self.create_contract()
        else:
            try:
                if self.client.get_client_cnp(client_cnp) is not None:
                    if self.package.search_package_title(package_name):
                        pak = self.package.search_package_title(package_name)
                        for p in pak:
                            pak_id = p.index
                            self.contract.create_contract(pak_id, package_name, client_cnp)
                    else:
                        print("Invalid package")
                else:
                    print("No such client")
            except ValueError as error:
                print(error)

    @make_highlight
    def random_client(self):
        no = int(input("Specify the number of randomly generated clients_file: "))
        for number in range(0, no):
            client = self.client.random_client_creator()
            self.client.create_client(client.name, client.surname, client.cnp)

    @make_highlight
    def random_package(self):
        no = int(input("Specify the number of randomly generated packages_file: "))
        for number in range(0, no):
            package = self.client.random_package_creator()
            self.package.create_package2(package.title, package.description, package.price)

    @make_highlight
    def search_contracts(self):
        index = input("Provide no of contract: ")
        if self.contract.search_contract(index) is not None:
            for i in self.contract.search_contract(index):
                print(i)
        else:
            print("No such contract")

    @make_highlight
    def display_contract(self):
        if self.contract.int_contract_list() is False:
            return False
        else:
            print("Contracts list:")
            self.contract.int_contract_list()

    @make_highlight
    def remove_contract(self):
        id = int(input("Provide contract ID: "))
        list = self.contract.delete_contract(id)
        return list


# Clients
clients_file = ClientsHandler("../FINAL_PROJ/clients.txt")
client_handling = ClientTools(clients_file)

# Packages
packages_file = PackageFileHandler("../FINAL_PROJ/packages.txt")
packages_handling = PackageTools(packages_file)

# Contracts
contracts_file = ContractsFileHandler("../FINAL_PROJ/contracts.txt")
contracts_handling = ContractTools(contracts_file)

u = UI(client_handling, packages_handling, contracts_handling)
# u.begin()
