import pandas as pd

'''
Using data from Eurostat, create a list of tuples representing the
"Self-perceived health by country and sex, age group >16, for people
living in cities" for 2017-2018.
Have at least 30 valoares in your dataset.
I exported the data needed from eurostat and deleted the information
we dont need then I modified the CSV file so that the lack of valoare
':' was replaced with 0
note: only "very good" perception was used.
The dataset will have the following structure:
[(country, year, sex, health_index) ]
'''

datainit = pd.read_csv('hlth_silc_01_1_Data.csv')
datasect = pd.DataFrame(datainit, columns=['GEO', 'TIME', 'SEX', 'Value'])
datalist = datasect.to_numpy().tolist()
print(datalist)
input()

# two dicts that group all data by country for each year
# health_index_2017 ={'France': [sex, health_index]}

# 1st solution
health_index_2017 = {
    '_'.join((geo, sex)): [valoare]
    for geo, timp, sex, valoare in datalist
    if timp == 2017
}
health_index_2018 = {
    '_'.join((geo, sex)): [valoare]
    for geo, timp, sex, valoare in datalist
    if timp == 2018
}
print(health_index_2017)
print(health_index_2018)
input()
# 2nd solution with 4 dict
health_index_2017_M = {
    geo: [valoare]
    for geo, timp, sex, valoare in datalist
    if timp == 2017
    if sex == 'M'
}
health_index_2017_F = {
    geo: [valoare]
    for geo, timp, sex, valoare in datalist
    if timp == 2017
    if sex == 'F'
}
health_index_2018_M = {
    geo: [valoare]
    for geo, timp, sex, valoare in datalist
    if timp == 2018
    if sex == 'M'
}
health_index_2018_F = {
    geo: [valoare]
    for geo, timp, sex, valoare in datalist
    if timp == 2018
    if sex == 'F'
}

# one dict that groups all data by year for Germany
# germany ={2017: [sex, health_index]}
country = sorted(list({geo for geo, timp, sex, valoare in datalist}))
print(country)


def hi_country(tara):
    tara = {
        '_'.join((str(timp), sex)): [valoare]
        for geo, timp, sex, valoare in datalist
        if geo == tara
    }
    return tara


for a_country in country:
    print(f'{a_country} - {hi_country(a_country)}')

# germany ={
#     str(timp)+'_'+sex: [valoare]
#     for geo, timp, sex, valoare in datalist
#     if geo == 'Germany'
# }
input()
print(f'Germany {hi_country("Germany")}')
input()
# one dict that grups all data by country and year,
# by using year in the key together with the country name
# health_index ={'France_2017': [year, sex, health_index]}

health_index = {
    "_".join((geo, str(timp), sex)): [timp, sex, valoare]
    for geo, timp, sex, valoare in datalist
}
print(health_index)
input()
# starting from the previous health_index dict, display only
# the data where the health_index > 5
print('\nhealth_index > 5\n')
for i in health_index.keys():
    if health_index[i][2] > 5:
        print(f'{i} {health_index[i]}')
input()
# starting from the previous health_index dict, display only
# the data where the health_index > 5 and sex is 'F'
print('\nhealth_index > 5 and sex is F\n')
for j in health_index.keys():
    if(health_index[j][2] > 5) and (health_index[j][1] == 'F'):
        print(f'{j} {health_index[j]}')
input()
# starting from the previous health_index dict, create a for
# loop to print the health_index
print('\nhealth_index\n')
for k in health_index.keys():
    print(f'{k} {health_index[k]}')
input()
