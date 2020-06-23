# Using data from Eurostat, create a list of tuples representing the "Self-perceived health by country and sex,
# age group >16, for people living in cities" for 2017-2018. Have at least 30 values in your dataset. The dataset will
# have the following structure: [ (country, year, sex, health_index) ]
# Example:  [('France', 2017, M, 12), ...]

import pandas as pd

# Create a data frame from original csv and choose only columns that interest us
df = pd.DataFrame(pd.read_csv('hlth_silc_01_1_Data.csv'), columns=('NO', 'GEO', 'TIME', 'SEX', 'Value', 'LEVELS'))

# Create a list of tuples for Dataframe rows using list comprehension
list_of_tuples = [tuple(row) for row in df.values]

# Print list of tuple
print(list_of_tuples)
# print(f'List contain {len(list_of_tuples)} rows')  # check length of list to have a reference
# print()  # empty row
#
# # two dicts that group all data by country for each year-> example: health_index_2017 = {'France': [sex, health_index]}
# # so year should be skipped
# # health index for 2017
# health_index_2017 = {
#     f'{country}_{sex}_{levels}': [sex, health_index]
#     for no, country, year, sex, health_index, levels in list_of_tuples
#     if year == 2017
# }
# print(health_index_2017)
# print(f'List contain {len(health_index_2017)} rows')  # check length of list to compare
# print('           ')  # empty row
#
# # health index for 2017
# health_index_2018 = {
#     f'{country}_{sex}_{levels}': [sex, health_index]
#     for no, country, year, sex, health_index, levels in list_of_tuples
#     if year == 2018
# }
# print(health_index_2018)
# print(f'List contain {len(health_index_2018)} rows')  # check length of list to compare
# print('           ')  # empty row


# one dict that groups all data by year for Germany. Example: germany = {2017: [sex, health_index]}
# 2017 is one unique key. we have to iterate to obtain multiple uniques keys
# Germany = {
#     f'{country}_{sex}_{levels}': [sex, health_index]
#     for no, country, year, sex, health_index, levels in list_of_tuples
#     if country == 'Germany' and year == 2017
# }
# print(Germany)
# print(f'List contain {len(Germany)} rows')  # check length of list to compare
# print('           ')  # empty row
#
# # one dict that groups all data by country and year, by using year in the key together with the country name
# # Example: health_index = {'France_2017': [year, sex, health_index]}
# health_index = {
#     f'{country}_{year}_#{no}': [year, sex, health_index]
#     for no, country, year, sex, health_index, levels in list_of_tuples
# }
#
# print(health_index)
# print(f'List contain {len(health_index)} rows')
# print()  # empty row
#
# # starting from the previous health_index dict, display only the data where the health_index > 5
# for k in health_index:
#     if health_index[k][2] > 5:
#         print(f'{k} : {str(health_index[k][1])}, {health_index[k][2]} > 5')
# print()  # empty row
#
# # starting from the previous health_index dict, display only the data where the health_index > 5 and sex is 'F'
# for k in health_index:
#     if health_index[k][2] > 5 and health_index[k][0] == 'Females':
#         print(f'{k} : {health_index[k][0]} , {str(health_index[k][1])} > 5')
# #
# print()  # empty row
#
# # starting from the previous health_index dict, create a for loop to print the health_index
# for k, v in health_index.items():
#     print(f'{k} : {v}')
