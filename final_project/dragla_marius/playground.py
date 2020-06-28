from final_project.dragla_marius.application import *

customers_category_sales = get_customer_category_sales("Invoice-report.csv")

category_sales = AllCategorySales.get_total_category_sales(customers_category_sales)

sales = Sales(category_sales)

customer_id_generator = generate_customer_id()

class_instantiator = instantiate_class(customers_category_sales, customer_id_generator, sales)

print(f'\nPlease select an option: \n1. Customer Sales \n2. Category Sales \n ')
print(sales)

print('\nPlease select customer ID or name for which you want to see the details \n')
print(sales.search_customer(input()))


print('\nPlease select what type of report you want to generate \n1. Customer Category Sales Report \n2. Total Sales Report \n')

with ReportGenerator(int(input()), sales) as file:
    contents = file.read()
    print(contents)


