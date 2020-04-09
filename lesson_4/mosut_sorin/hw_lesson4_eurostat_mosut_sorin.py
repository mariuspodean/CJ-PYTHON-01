# import pakcage for Excel files
import csv
from pprint import pprint

# function to detect if a string can be converted into a float

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

# python object for Excel file

eurostat_file = open('hlth_silc_01_1_Data.csv')
csv_reader_object = csv.reader(eurostat_file)

# list with data from Excel file [country, year, sex (M/F), health_index]

tuple_list_data = [
                   [line[1] , int(line[0]) , str(line[4])[0] , float(line[7])]
                   for line in csv_reader_object
                  ]
pprint(tuple_list_data)
print()


# tuple with all the countryes from file

tuple_countryes = []
for line in tuple_list_data:
    if not line[0] in tuple_countryes:
            tuple_countryes.append(line[0])
tuple_countryes.sort()
tuple_countryes = tuple(tuple_countryes)
pprint(tuple_countryes)
print()

# tuple with all the years from file

tuple_years = []
for line in tuple_list_data:
    if not line[1] in tuple_years:
            tuple_years.append(line[1])
tuple_years.sort()
tuple_years = tuple(tuple_years)
pprint(tuple_years)


# adding an serial number and year to each country name si transformare lista de liste in lista de tuple

y = 1
for x in range(len(tuple_list_data)-1):
    if tuple_list_data[x][0] == tuple_list_data[x + 1][0]:
        if y < 10:
            tuple_list_data[x][0] += '_' + str(tuple_list_data[x][1])[2:4] + '_0' + str(y)
            y += 1
            tuple_list_data[x] = tuple(tuple_list_data[x])
    else:        
        tuple_list_data[x][0] += '_' + str(tuple_list_data[x][1])[2:4] + '_' + str(y)
        y = 1
        tuple_list_data[x] = tuple(tuple_list_data[x])
        
tuple_list_data[len(tuple_list_data) - 1][0] += '_' + str(tuple_list_data[x][1])[2:4] + '_' + str(y)
tuple_list_data[len(tuple_list_data) - 1] = tuple(tuple_list_data[len(tuple_list_data) - 1])
pprint(tuple_list_data)
print()


# dict with key = country and value a list with sex and health index for a specified year
 
year = input('\nIntrodu anul pentru care doresti sa se creeze dictionarul: ')
while year != 'x':
    while str.isnumeric(year): 
        year = int(year)
        if year in tuple_years:
            health_index_years = {
                        tuple1[0]: [tuple1[2] , tuple1[3]]
                        for tuple1 in tuple_list_data
                        if tuple1[1] == year
                        }
            for dict_years in health_index_years:
                print(f'{(str(dict_years)[0:len(str(dict_years)) - 6]).ljust(16)} {health_index_years[dict_years]}')
            print('\n')
            year = input('Pentru a trece la pasul urmator introdu '' x''\nIntrodu anul pentru care doresti sa se creeze dictionarul: ')
            if year == 'x':
                break
        else:
            print('\nAnul introdus nu e valid, introdu alt an\nPentru a trece la pasul urmator introdu '' x'' ')
            year = input('Introdu anul pentru care doresti sa se creeze dictionarul: ')
            if year == 'x':
                break
    else:
        print('\nAi folosit caractere string, introdu alt an\nPentru a trece la pasul urmator introdu '' x'' ')
        year = input('Introdu anul pentru care doresti sa se creeze dictionarul: ')
        if year == 'x':
            break

# dict with key = country + year and value a list with sex and health index for a specified country

country_name = str(input(f'\nLsta tari : {tuple_countryes}\nIntrodu tara in functie de care sa se creeze dictionarul : '))
while country_name != 'x':    
    while str.title(country_name) in tuple_countryes:
        country_health_index = {
                            tuple4[0]: [tuple4[2] , tuple4[3]]
                            for tuple4 in tuple_list_data
                            if tuple4[0].startswith(str.title(country_name))
                            }
        for dict_country in country_health_index:
            print(f'{(str(dict_country)[0:len(str(dict_country)) - 3]).ljust(16)} {country_health_index[dict_country]}')
        country_name = str(input(f'\nLsta tari : ({tuple_countryes})\n\nPentru a trece la pasul urmator introdu '' x''\nIntrodu tara in functie de care sa se creeze dictionarul : '))
        if country_name == 'x':
            break
    else:
        print('\nTara introdusa nu e valida, introdu alta Tara\nPentru a trece la pasul urmator introdu '' x'' ')
        country_name = str(input(f'Introdu tara in functie de care sa se creeze dictionarul : '))

# dict with key = tara_an and values list with year , sex , health index

health_index = {
                tuple5[0] : [tuple5[1] , tuple5[2] , tuple5[3]]
                for tuple5 in tuple_list_data                
                }

# print all data with health index > a specified valua

health_index_input1 = str(input('\nPentru a trece la pasul urmator introdu '' x''\nIntroduceti valoarea indexului de sanatate de referinta in functie de care sa se printeze rezultatele: '))
while health_index_input1 != 'x':
    while isfloat(health_index_input1):
        health_index_input1 = float(health_index_input1)
        print('\n')
        for dict1 in health_index:
            if health_index[dict1][2] > health_index_input1:
                print(f'{(str(dict1)[0:len(str(dict1)) - 6]).ljust(16)} {health_index[dict1]}')
        health_index_input1 = str(input('\nPentru a trece la pasul urmator introdu '' x''\nIntroduceti valoarea indexului de sanatate de referinta in functie de care sa se printeze rezultatele: '))
        if health_index_input1 == 'x':
            break
    else:
        print('\nValoare indexului de sanatate nu e valida, introdu alta valoare')
        health_index_input1 = str(input('\nPentru a trece la pasul urmator introdu '' x''\nIntroduceti valoarea indexului de sanatate de referinta in functie de care sa se printeze rezultatele: '))

# print all data with health index > a specified valua and sex

health_index_input2 = str(input('\nIntroduceti valoarea indexului de sanatate de referinta in functie de care sa se printeze rezultatele: '))
sex_index = str(input('Introduceti genul persoanelor referinta in functie de care sa se printeze rezultatele M/F: '))
while health_index_input2 != 'x':
    while isfloat(health_index_input2) and sex_index in {'m', 'f', 'M', 'F'}:
        health_index_input2 = float(health_index_input2)
        print('\n')
        for dict1 in health_index:
            if health_index[dict1][2] > health_index_input2 and health_index[dict1][1] == str.title(sex_index) :
                print(f'{(str(dict1)[0:len(str(dict1)) - 6]).ljust(16)} {health_index[dict1]}')
        health_index_input2 = str(input('\nPentru a trece la pasul urmator introduceti '' x ''\nIntroduceti valoarea indexului de sanatate de referinta in functie de care sa se printeze rezultatele: '))
        if health_index_input2 == 'x':
            break
        sex_index = str(input('Introduceti genul persoanelor referinta in functie de care sa se printeze rezultatele M/F: '))
    else:
        print('\nValorile introduse nu sunt valide, inrodu alte valor')
        health_index_input2 = str(input('\nIntroduceti valoarea indexului de sanatate de referinta in functie de care sa se printeze rezultatele: '))
        sex_index = str(input('Introduceti genul persoanelor referinta in functie de care sa se printeze rezultatele M/F: '))
        
# print all data from health_index dict

interogare = str(input('\nPrintare date complete [DA/NU]: '))
print('\n')
if interogare == 'DA' or interogare == 'da':   
    for dict1 in health_index:
        print(f'{(str(dict1)[0:len(str(dict1)) - 6]).ljust(16)} {health_index[dict1]}')












