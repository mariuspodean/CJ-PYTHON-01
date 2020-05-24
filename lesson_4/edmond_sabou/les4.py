# The dataset will have the following structure:
#
# [ (country, year, sex, health_index) ]
#
# Example:
#
# [('France', 2017, M, 12), ...]
#

dataset = [('Belgium_M', 2017, 'Males', 33.2), ('Bulgaria_M', 2017, 'Males', 24.4), ('Czech_M', 2017, 'Males', 22.8),
           ('Denmark_M', 2017, 'Males', 26.8), ('Germany_M', 2017, 'Males', 19.8), ('Estonia_M', 2017, 'Males', 10.6),
           ('Ireland_M', 2017, 'Males', 44.5), ('Greece_M', 2017, 'Males', 47.4), ('Spain_M', 2017, 'Males', 20.5),
           ('France_M', 2017, 'Males', 26.3), ('Croatia_M', 2017, 'Males', 30.8), ('Italy_M', 2017, 'Males', 15.1),
           ('Cyprus_M', 2017, 'Males', 50.5), ('Latvia_M', 2017, 'Males', 4.3), ('Lithuania_M', 2017, 'Males', 9.1),
           ('Belgium_F', 2017, 'Females', 28.4), ('Bulgaria_F', 2017, 'Females', 19.1),
           ('Czech_F', 2017, 'Females', 18.4), ('Denmark_F', 2017, 'Females', 24.4),
           ('Germany_F', 2017, 'Females', 17.3), ('Estonia_F', 2017, 'Females', 11.3),
           ('Ireland_F', 2017, 'Females', 44.8), ('Greece_F', 2017, 'Females', 42.8),
           ('Spain_F', 2017, 'Females', 17.7), ('France_F', 2017, 'Females', 22.4),
           ('Croatia_F', 2017, 'Females', 25.5), ('Italy_F', 2017, 'Females', 12.2),
           ('Cyprus_F', 2017, 'Females', 48.7), ('Latvia_F', 2017, 'Females', 2.8),
           ('Lithuania_F', 2017, 'Females', 6.2), ('Belgium_F', 2018, 'Females', 26.4),
           ('Bulgaria_F', 2018, 'Females', 17.1), ('Czech_F', 2018, 'Females', 18.2),
           ('Denmark_F', 2018, 'Females', 24.7), ('Germany_F', 2018, 'Females', 17.3),
           ('Estonia_F', 2018, 'Females', 8.4), ('Ireland_F', 2018, 'Females', 45.5),
           ('Greece_F', 2018, 'Females', 44.1), ('Spain_F', 2018, 'Females', 21.1), ('France_F', 2018, 'Females', 21.7),
           ('Croatia_F', 2018, 'Females', 26.2), ('Italy_F', 2018, 'Females', 13.6),
           ('Cyprus_F', 2018, 'Females', 45.3), ('Latvia_F', 2018, 'Females', 4.4),
           ('Lithuania_F', 2018, 'Females', 5.7), ('Belgium_M', 2018, 'Males', 30.5),
           ('Bulgaria_M', 2018, 'Males', 22.2), ('Czech_M', 2018, 'Males', 22.1),
           ('Denmark_M', 2018, 'Males', 27.4), ('Germany_M', 2018, 'Males', 18.5), ('Estonia_M', 2018, 'Males', 9.3),
           ('Ireland_M', 2018, 'Males', 45.7), ('Greece_M', 2018, 'Males', 48.1), ('Spain_M', 2018, 'Males', 24.1),
           ('France_M', 2018, 'Males', 24.3), ('Croatia_M', 2018, 'Males', 31.2), ('Italy_M', 2018, 'Males', 16.4),
           ('Cyprus_M', 2018, 'Males', 47.9), ('Latvia_M', 2018, 'Males', 6.8), ('Lithuania_M', 2018, 'Males', 9.0)]

# Using only comprehensions, create the following dicts:
#
# two dicts that group all data by country for each year
# health_index_2017 = {'France': [sex, health_index]}
#
# health_index_2018 = {'France': [sex, health_index]}
health_index_2017 = {
    country: [sex, health_index]
    for country, year, sex, health_index in dataset
    if year == 2017
}

health_index_2018 = {
    country: [sex, health_index]
    for country, year, sex, health_index in dataset
    if year == 2018
}

# one dict that groups all data by year for Germany
# germany = {2017: [sex, health_index]}
germany_M = {year: [sex, health_index]
             for country, year, sex, health_index in dataset
             if year == 2017 and country == "Germany_M"
             }

germany_F = {year: [sex, health_index]
             for country, year, sex, health_index in dataset
             if year == 2017 and country == "Germany_F"
             }

germany_M2 = {year: [sex, health_index]
              for country, year, sex, health_index in dataset
              if year == 2018 and country == "Germany_M"
              }

germany_F2 = {year: [sex, health_index]
              for country, year, sex, health_index in dataset
              if year == 2018 and country == "Germany_M"
              }

# one dict that groups all data by country and year, by using year in the key together with the country name
# health_index = {'France_2017': [year, sex, health_index]}
#
health_index = {
    country + "_2017": [year, sex, health_index]
    for country, year, sex, health_index in dataset
    if year == 2017
}

health_index2 = {
    country + "_2018": [year, sex, health_index]
    for country, year, sex, health_index in dataset
    if year == 2018
}

# starting from the previous health_index dict, display only the data where the health_index > 5
#
above5 = {
    country: value for country, value in health_index.items() if value[2] > 40
}
print(above5)

# starting from the previous health_index dict, display only the data where the health_index > 5 and sex is 'F'
#
above5f = {
    country: value for country, value in health_index.items() if value[2] > 40 and value[1] == "Females"
}
print(above5f)

# starting from the previous health_index dict, create a for loop to print the health_index
#
for value1, value2, value3 in health_index.values():
    print(value3)
