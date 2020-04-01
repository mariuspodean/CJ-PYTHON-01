# import pakcage for Excel files
import csv
import pep8
from pprint import pprint

fchecker = pep8.Checker('functions_homework.py', show_source=True)
file_errors = fchecker.check_all()

if file_errors:
    print("Found %s errors (and warnings)" % file_errors)

# python object for Excel file

cuntryes_abr_file = open('countryes_abrev.csv')
csv_reader_object = csv.reader(cuntryes_abr_file)

# list with data from Excel file with countryes names and abreviations

cuntryes_abr_list = [
                      [line[0], line[1]]
                      for line in csv_reader_object
                    ]

cuntryes_abr_file.close()

# data set

description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ',
                           '2016 ', '2017 ', '2018 ', '2019 '])

raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 b']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('GR', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 b']),
]

# check_cover function check each 'coverage' value and formates it


def check_cover_value(cover_in):
    cover = ''
    if str.isnumeric(cover_in):
        return int(cover_in)
    elif cover_in.find(':') != -1:
        return 0
    else:
        for iter_0 in range(len(cover_in)):
            if str.isnumeric(cover_in[iter_0]):
                cover += cover_in[iter_0]
            else:
                break
        return cover

# cover_value_int lamda function convert the 'coverage' value in integer

cover_value_int = lambda arg_1, arg_2: int(check_cover_value(
    str.strip(raw_data[arg_1][1][len(raw_data[1][1]) - 1 - arg_2])))

"""
dict_year_cover function creates a list of dicts with key = year and
value = coverage for each year
"""


def list_dict_year_cover(arg_iter_1):
    return [
             {
                'year': str.strip(description[1]
                                  [len(raw_data[1][1]) - 1 - iter_2]),
                'coverage': cover_value_int(arg_iter_1, iter_2)
              }
             for iter_2 in range(len(raw_data[1][1]))
            ]

# create_dataset_dict function creates the main dict with al dates


def create_dataset_dict(arg_dict):
    return {country_abr[1]: list_dict_year_cover(iter_2)
            for iter_2 in range(len(arg_dict))
            for country_abr in cuntryes_abr_list
            if arg_dict[iter_2][0] == country_abr[0]
            }


dict_dataset = create_dataset_dict(raw_data)

for print_data in dict_dataset:
    print('\n\n', print_data, '\n')
    iter_1 = 0
    for print_data2 in dict_dataset[print_data]:
        print(print_data2, end=' ')
        iter_1 += 1
        if iter_1 % 3 == 0 and iter_1 < len(dict_dataset[print_data]):
            print()

# get_year_data function to retrieve data for a year introduced by user

year_in = input('\nIntroduceti anul pentru care'
                'doriti sa obtineti valorile acoperirii : ')


def get_year_data(dataset, year):
    return {year: [[country, data_cover['coverage']]
                   for country in dataset
                   for data_cover in dataset[country]
                   if data_cover['year'] == str(year)
                   ]
            }

dict_year_data = get_year_data(create_dataset_dict(raw_data), year_in)

for print_data in dict_year_data:
    print('\n', print_data, ':\n')
    print('Country'.ljust(25), 'Coverage\n')
    for print_data2 in dict_year_data[print_data]:
        print(print_data2[0].ljust(25), ' = ', print_data2[1])

"""
get_country_data function to retrieve data for a
specific country name introduced by user
"""

country_in = input('\nIntroduceti tara pentru care doriti'
                   'sa obtineti valorile anuale ale acoperirii : ').title()


def get_country_data(dataset, country_arg):
    return {country_arg: [[data_country['year'], data_country['coverage']]
                          for data_country in dataset[country_arg]
                          ]
            }

dict_coutry_year_data = get_country_data(create_dataset_dict(raw_data),
                                         country_in)

for print_data in dict_coutry_year_data:
    print('\n', print_data, '\n')
    print('Year'.ljust(6), 'Coverage\n')
    for print_data2 in dict_coutry_year_data[print_data]:
        print(print_data2[0], ' = ', print_data2[1])

# input country for wich to calculte the average

country = input('\nIntroduceti tara pentru care'
                'doriti sa obtineti media acoperirii : ').title()

# country_data list with values for calculation of the average

country_data = [data_list[1] for data_list in get_country_data
                (create_dataset_dict(raw_data), country)[country]]

"""
perform_average function , return the average of coverage in a period of time
for a individual country
"""


def perform_average(*cover_values):
    contor = 0
    for values_dif_zero in cover_values[0]:
        if values_dif_zero > 0:
            contor += 1
    return sum(cover_values[0]) / contor

average = perform_average(country_data)

print('\nMedia acoperiri in {} in perioada {}- {} este {:.2f}'.
      format(country, description[1][0],
             description[1][len(description[1])-1], average))
