health_dataset = [('Germany', 2017, 'M', 19.8), ('Ireland', 2017, 'M', 44.5),
                  ('Spain', 2017, 'M', 20.5), ('France', 2017, 'M', 26.3),
                  ('Italy', 2017, 'M', 15.1), ('Germany', 2018, 'M', 18.5),
                  ('Estonia', 2017, 'M', 10.6), ('Netherlands', 2018, 'M', 24.6),
                  ('Slovakia', 2018, 'M', 25.7), ('Montenegro', 2017, 'M', 44.0),
                  ('Serbia', 2018, 'M', 21.0), ('Romania', 2018, 'M', 45.7),
                  ('United Kingdom', 2018, 'M', 40.0),
                  ('Austria', 2018, 'M', 73.2), ('Bulgaria', 2017, 'M', 46.1),
                  ('Germany', 2017, 'F', 17.3), ('Ireland', 2017, 'F', 44.8),
                  ('Spain', 2017, 'F', 17.7), ('Turkey', 2017, 'F', 4.5),
                  ('Italy', 2017, 'F', 12.2), ('Romania', 2017, 'F', 22.4),
                  ('Norway', 2017, 'F', 28.5), ('Austria', 2018, 'F', 31.1),
                  ('Belgium', 2018, 'F', 26.4), ('Denmark', 2018, 'F', 24.7),
                  ('Greece', 2018, 'F', 44.1), ('Luxemburg', 2018, 'F', 23.3),
                  ('Hungary', 2018, 'F', 14.1), ('Poland', 2018, 'F', 14.2),
                  ('Switzerland', 2018, 'F', 33.7)]

health_index_2017 = {
    '_'.join([country, sex]): [sex, health_index]
    for country, year, sex, health_index in health_dataset
    if year == 2017
}
print(health_index_2017)

health_index_2018 = {
    '_'.join([country, sex]): [sex, health_index]
    for country, year, sex, health_index in health_dataset
    if year == 2018
}
print(health_index_2018)

germany = {
    '_'.join([sex, str(year)]): [sex, health_index]
    for country, year, sex, health_index in health_dataset
    if country == 'Germany'
}
print('Germany: ', germany)

health_index = {
    '_'.join([country, sex, str(year)]): [year, sex, health_index]
    for country, year, sex, health_index in health_dataset
}
print('Health Index:\n', health_index)

health_index_1 = {
    country: values_set
    for country, values_set in health_index.items()
    if values_set[2] > 40
}
print('Health Index > 40:\n', health_index_1)

health_index_2 = {
    country: values_set
    for country, values_set in health_index.items()
    if values_set[2] > 40 and values_set[1] == 'F'
}
print('Health Index > 40 && sex == F:\n', health_index_2)

print('Health Index in For Loop')
for e in health_index.values():
    print(e[2])
