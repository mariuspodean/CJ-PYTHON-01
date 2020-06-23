countrys = [
    'Belgium', 'Bulgaria', 'Czechia', 'Denmark', 'Germany', 'Estonia', 'Ireland',
    'Greece', 'Spain', 'France', 'Croatia', 'Italy', 'Cyprus', 'Latvia', 'Lithuania',
    'Luxembourg', 'Hungary', 'Malta', 'Netherlands', 'Austria', 'Poland', 'Portugal',
    'Romania', 'Slovenia', 'Slovakia', 'Finland', 'Sweden', 'United Kingdom', 'Iceland',
    'Norway'
]


years = [
    2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017,
    2017, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018,
    2018, 2018
]


health_indexes = [
    16.4, 25.0, 16.3, 9.3, 42.0, 42.7, 13.9, 20.2, 23.2, 9.7, 44.0, 4.4, 5.5, 21.4, 14.7,
    21.5, 20.5, 31.1, 14.1, 7.6, 23.0, 18.3, 20.6, 19.0, 27.9, 30.5, 35.7, 28.8, 31.0, 37.0
]


sexes = [
    'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F',
    'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'
]


data_sequence = list(zip(countrys, years, sexes, health_indexes))

print(data_sequence)


dict_data = {
           country:[year, sex, health_index] for country, year, sex, health_index in
data_sequence
}

print(dict_data)


aa = {
   country: [health_index] for country, _, _, health_index in data_sequence if
health_index > 5
}

print(aa)


bb = {
   country: [sex, health_index] for country, _, sex, health_index in data_sequence if
health_index >5 and sex == 'F'
}

print(bb)


cc = {
   country: [year, sex, health_index] for country, year, sex, health_index in
data_sequence if year == 2017
}

print(cc)


dd = {
   country: [year, sex, health_index] for country, year, sex, health_index in
data_sequence if year == 2018
}

print(dd)


ee = {
   country: [year, sex, health_index] for country, year, sex, health_index in
data_sequence if country == 'Germany'
}

print(ee)


ff = {
  (country, year): [sex, health_index] for country, year, sex, health_index
in data_sequence
}

print(ff)


for x, y, z in dic_data.values():
    print(z)
    
