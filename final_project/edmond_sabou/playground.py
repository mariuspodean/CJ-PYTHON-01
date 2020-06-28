from final_project.edmond_sabou.application import *

# clients
client = Client(12, "Name", "Surname", "6663338889365")
print(client)
clients_file.store_client(client)
u.interrogate_client_list()
clients_file.find_client(6663338889365)
u.interrogate_client_list()
client_handling.update_client("6663338889365", "New_Name", "New_Surname", "2222222222222")
u.interrogate_client_list()
clients_file.remove_client("2222222222222")
u.interrogate_client_list()

# packages
package = TouristicPackage(1, "PackageName", "PackageDescription", 999)
print(package)
title = "PackageName"
description = "PackageDescription"
price = 999
packages_handling.create_package2(title, description, price)
print(packages_file.size_packages())
u.interrogate_package_list()
packages_handling.search_package_title("PackageName")
packages_file.remove_package("PackageName")
print(packages_file.size_packages())
u.interrogate_package_list()

# contracts
u.interrogate_contract_list()
contracts_handling.create_contract(1, "First", "1234567890123")
u.interrogate_contract_list()
contracts_handling.delete_contract(1)

u.begin()
