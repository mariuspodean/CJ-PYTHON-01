# import pakcage for Excel files
import csv
import pep8
from pprint import pprint

# clean code check
fchecker = pep8.Checker('functions_homework.py', show_source=True)
file_errors = fchecker.check_all()

if file_errors:
    print("Found %s errors (and warnings)" % file_errors)

# python object for Excel file
countryes_abr = open('countryes_abrev.csv')
csv_reader_object = csv.reader(countryes_abr)

# list with data from Excel file with countryes names and abreviations
countryes_abr_list = [
    [line[0], line[1]]
    for line in csv_reader_object
]
countryes_abr.close()

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


# list_dict_yearcoverage function creates a list of disct with year and coverage as values


def list_dict_yearcoverage(raw_data_in, tara):
    return [
        {
            'year': str.strip(description[1][z[0]]),
            'coverage': z[1].strip(" :b")

        }

        for x in enumerate(raw_data_in)
        for z in enumerate(x[1][1])
        if tara == x[1][0]
    ]


# dataset_dict function creates the main dataset dict


def dataset_dict(raw_data_in):
    return {tara2[1]: list_dict_yearcoverage(raw_data_in, tara[0])
            for tara in raw_data_in
            for tara2 in countryes_abr_list
            if tara[0] == tara2[0]
            }


# get_year_data function to retrieve coverage data for a year introduced by user


def get_year_data(data_set, year):
    return {year: [[country, data_coverage['coverage']]
                   for country in data_set
                   for data_coverage in data_set[country]
                   if data_coverage['year'] == str(year)
                   ]
            }


# get_country_data function to retrieve data for a specific country name introduced by user


def get_country_data(data_set, country_arg):
    return {country_arg: [[data_country['year'], data_country['coverage']]
                          for data_country in data_set[country_arg]
                          ]
            }


# perform_average_country function calculate the average of coverage for a specified country on all years


def perform_average_country(country_year_data, country_in):
    coverage_list = [cover_iter[1] for cover_iter in country_year_data[country_in]]
    coverage_list = [int(cover_iter) for cover_iter in coverage_list if cover_iter]
    average = sum(coverage_list) / len(coverage_list)
    return average


# perform_average_year function calculate the average of coverage for a specified country on all years


def perform_average_year(country_coverage_in, year):
    coverage_list = [cover_iter[1] for cover_iter in country_coverage_in[year]]
    coverage_list = [int(cover_iter) for cover_iter in coverage_list if cover_iter]
    average = sum(coverage_list) / len(coverage_list)
    return average


# create dataset main dic
dict_dataset = dataset_dict(raw_data)
pprint(dict_dataset)

# input year for wich to print the coverage values
year_in = input('\nIntroduceti anul pentru care doriti sa obtineti valorile acoperirii: ')

# obtain the dict with the values for the year specified above
dict_year_data = get_year_data(dataset_dict(raw_data), year_in)
print()
pprint(dict_year_data)

# input country for wich to print the coverage values
country_in = input('\nIntroduceti tara pentru care doriti sa obtineti valorile anuale ale acoperirii: ').title()

# obtain the dict with values for the country specified above
dict_coutry_year_data = get_country_data(dataset_dict(raw_data), country_in)
print()
pprint(dict_coutry_year_data)
# input country for wich to calculte the average, obtain the value and print it
country = input('\nIntroduceti tara pentru care doriti sa obtineti media acoperirii: ').title()
country_average = perform_average_country(dict_coutry_year_data, country)
print('\nMedia acoperiri in {} in perioada {}- {} este: {:.2f}'.format
      (country, description[1][0], description[1][len(description[1]) - 1], country_average))

# input year for wich to calculte the average, obtain the value and print it
year = input('\nIntroduceti anul pentru care doriti sa obtineti media acoperirii : ')
country_coverage = get_year_data(dict_dataset, year)
year_average = perform_average_year(country_coverage, year)
print('\nMedia acoperiri in Europa pentru anul {} este: {:.2f}'.format(year, year_average))
