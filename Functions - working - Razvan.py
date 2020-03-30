"""
For this exercise we will perform some data aggregation tasks, on data from eurostat regarding internet access coverage.
Tasks:
Average/year
Average/country
"""
from collections import defaultdict

description = ['Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
    '2019 '
]]

# reduce raw data to have a clear image how everything is working
raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 '])

]

type_average_list = ['Year', 'Country']

# create global variables that can be used in perform_average function
dataset1 = []
list_year = []
len_list_year = []
list_country = []
len_list_country = []


# This function will take the raw dataset as an argument
# This function will return a dict with the following structure FAIL !!!
# # {'Romania': [{'year': '2019','coverage': 84}, {'year': '2018','coverage': 67},..., {'year': '2011','coverage': 72}],

def listToDict(rawdata_input):
    global dataset1
    # create dataset
    dataset1 = {country: dict(zip(description[1], coverage)) for country, coverage in rawdata_input}
    return dataset1


# function to retrieve data for each year
# This function will take the dataset and year as an argument.

def retrieve_data_for_year(year):
    global len_list_year, dataset1, list_year
    # loop through dataset values
    for item1 in dataset1.keys():
        list_year.append((item1, dataset1[item1][year]))
        len_list_year = len(list_year)
    return [f'Data for {year} is: {list_year}'], [len_list_year]


# function to retrieve data for each country
# This function will take the dataset and country as an argument.

def retrieve_data_for_country(country):
    global len_list_country, dataset1, list_country
    for item2 in dataset1[country]:
        list_country.append((item2, dataset1[country][year]))
        len_list_country = len(list_country)
    return [f'Data for {country} is: {list(list_country)}'], [len_list_country]

# function to perform average from an iterable(of year data or country data)
# This function will take an iterable as an argument

def QuestionOne():
    # check (search) if some item is in list; let user choose what is searching for
    print('Do you want to perform average by : ')
    for number, item in enumerate(type_average_list):
        print(f'{number + 1}: {item}')


def perform_average():
    global list_year, len_list_year, list_country, len_list_country
    QuestionOne()
    question_one_input = int(input())
    value = 0
    if question_one_input == 1:
        for (item, value) in list_year:
            if value != ': ' and int(value) > 0:
                value += int(value[:-1])
                value2 = value / len_list_year
    elif question_one_input == 2:
        for (item, value) in list_country:
            if value != ': ' and int(value) > 0:
                value += int(value[:-1])
                value2 = value / len_list_country
    return value2

datas = listToDict(raw_data)
print(datas)
print()
year = '2018 '
country = 'AL'
data_for_year = retrieve_data_for_year(year)
print(data_for_year)
print(len_list_year)
print()
data_for_country = retrieve_data_for_country(country)
print(data_for_country)
print(len_list_country)
print()
perform_average()
