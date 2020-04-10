from collections import defaultdict

self_perceived_health = [
    ('Belgium', 2017, 'F', 28.4), ('Belgium', 2018, 'F', 26.4),
    ('Belgium', 2017, 'M', 33.2), ('Belgium', 2018, 'M', 30.5),
    ('Italy', 2017, 'F', 12.2), ('Italy', 2018, 'F', 13.6),
    ('Italy', 2017, 'M', 15.1), ('Italy', 2018, 'M', 16.4),
    ('Malta', 2017, 'F', 26.4), ('Malta', 2018, 'F', 22.5),
    ('Malta', 2017, 'M', 30.6), ('Malta', 2018, 'M', 26.3),
    ('Cyprus', 2017, 'F', 48.7), ('Cyprus', 2018, 'F', 45.3),
    ('Cyprus', 2017, 'M', 50.5), ('Cyprus', 2018, 'M', 47.9),
    ('Romania', 2017, 'F', 24.4), ('Romania', 2018, 'F', 22.9),
    ('Romania', 2017, 'M', 31.5), ('Romania', 2018, 'M', 30.2),
    ('Hungary', 2017, 'F', 14.1), ('Hungary', 2018, 'F',14.1),
    ('Hungary', 2017, 'M', 20.4), ('Hungary', 2018, 'M', 18.5),
    ('Netherlands', 2017, 'F', 20.1), ('Netherlands', 2018, 'F', 20.2),
    ('Netherlands', 2017, 'M', 24.6), ('Netherlands', 2018, 'M', 26.9),
    ('Sweden', 2017, 'F', 27.7), ('Sweden', 2018, 'F', 26.7),
    ('Sweden', 2017, 'M', 30.2), ('Sweden', 2018, 'M', 31.7),
    ('Finland', 2017, 'F', 19.2), ('Finland', 2018, 'F', 16.5),
    ('Finland', 2017, 'M', 20.2), ('Finland', 2018, 'M', 19.4),
    ('Germany', 2017, 'F', 28.5), ('Germany', 2018, 'F', 27.4),
    ('Germany', 2017, 'M', 27.9), ('Germany', 2018, 'M', 28.8)
]

year_2017 = defaultdict(list)
year_2018 = defaultdict(list)
romania = defaultdict(list)
countries_by_year = defaultdict(list)

#Group all data by year
year_2017 = {
    country + '_' + sex: [sex, year, index]
    for country, year, sex, index in self_perceived_health if year == 2017
}
print(year_2017)

year_2018 = {
    country +'_' + sex: [sex, year, index]
    for country, year, sex, index in self_perceived_health if year == 2018
}
print(year_2018)
print('-------------------------------')
#1 dict for specific country
romania = {
    str(year) + '_' + sex: [year, sex, index]
    for country, year, sex, index in self_perceived_health if country == 'Romania'
}
print(romania)
print('-------------------------------')

#All data by country and year with the country name and key togheter
countries_by_year = {
    country + '_' + str(year) + '_' + sex: [year, sex, index]
    for country, year, sex, index in self_perceived_health
}
print(countries_by_year)
print('-------------------------------')
#Only the data where index > 5
for data in countries_by_year.keys():
    if countries_by_year[data][2] > 25:
        print(data + '_' + str(countries_by_year[data]))
print('-------------------------------')

#Only the data where index >5 and is 'F'
for data2 in countries_by_year.keys():
    if countries_by_year[data2][2] > 25 and (countries_by_year[data2][1] == 'F'):
        print(data2 + '_' + str(countries_by_year[data2]))
print('-------------------------------')

#Loop
for data3 in countries_by_year.keys():
    print(data3 + '_' + str(countries_by_year[data3]))
    
print('the end')
