"""
For this exercise we will perform some data aggregation tasks, on data from eurostat regarding internet access coverage.
Tasks:
Average/year
Average/country
"""
import pprint

description = ['Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
    '2019 '
]]

# reduce raw data to have a clear image how everything is working

raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 '])
]


# This function will take the raw dataset as an argument
# This function will return a dict with the following structure :
# # {'Romania': [{'year': '2019','coverage': 84}, {'year': '2018','coverage': 67},..., {'year': '2011','coverage': 72}],
# According with what we've learned.
# Author: George Dragan
def list_to_dict(raw_data):
    dataset1 = {
        country: [{'year': year, 'coverage': coverage} for year, coverage in enumerate(data_coverage, start=2011)]
        for country, data_coverage in raw_data
    }
    return dataset1


def retrieve_data_for_year(dataset1, year):
    dict_year = {
        year: [(country, index['coverage'])
               for country in dataset1.keys()
               for index in dataset1[country]
               if index['year'] == year]
    }
    return dict_year


def retrieve_data_for_country(dataset1, country):
    dict_country = {
        country: [(item['year'], item['coverage'])
                  for item in dataset1[country]]
    }
    return dict_country


# -------------- user input ----------------------------

dataset1 = list_to_dict(raw_data)
print(dataset1)
print()

year = 2018
country = 'AT'
data_for_year = retrieve_data_for_year(dataset1, year)
print(data_for_year)
print()

data_for_country = retrieve_data_for_country(dataset1, country)
print(data_for_country)
