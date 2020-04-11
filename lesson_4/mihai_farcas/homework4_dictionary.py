a=(('Belgium',2017,'M',33), 
('Belgium',2017,'M',44), 
('Belgium',2017,'M',78), 
('Belgium',2017,'M',16), 
('Belgium',2017,'M',6), 
('Belgium',2017,'M',1                 ), 
('Belgium',2017,'M',7), 
('Belgium',2017,'F',28), 
('Belgium',2017,'F',43), 
('Belgium',2017,'F',71), 
('Belgium',2017,'F',19), 
('Belgium',2017,'F',8),
('Belgium',2017,'F',2), 
('Belgium',2017,'F',10), 
('Germany',2017,'M',20), 
('Germany',2017,'M',47), 
('Germany',2017,'M',67), 
('Germany',2017,'M',25), 
('Germany',2017,'M',7), 
('Germany',2017,'M',2), 
('Germany',2017,'M',8), 
('Germany',2017,'F',17), 
('Germany',2017,'F',47), 
('Germany',2017,'F',64), 
('Germany',2017,'F',28), 
('Germany',2017,'F',7), 
('Germany',2017,'F',2), 
('Germany',2017,'F',9), 
('Belgium',2018,'M',31), 
('Belgium',2018,'M',47), 
('Belgium',2018,'M',77), 
('Belgium',2018,'M',15), 
('Belgium',2018,'M',6), 
('Belgium',2018,'M',2), 
('Belgium',2018,'M',7), 
('Belgium',2018,'F',26), 
('Belgium',2018,'F',46), 
('Belgium',2018,'F',72), 
('Belgium',2018,'F',17), 
('Belgium',2018,'F',9), 
('Belgium',2018,'F',2), 
('Belgium',2018,'F',10), 
('Germany',2018,'M',19), 
('Germany',2018,'M',48), 
('Germany',2018,'M',67), 
('Germany',2018,'M',25), 
('Germany',2018,'M',7), 
('Germany',2018,'M',1), 
('Germany',2018,'M',8), 
('Germany',2018,'F',17), 
('Germany',2018,'F',47), 
('Germany',2018,'F',64), 
('Germany',2018,'F',27), 
('Germany',2018,'F',7), 
('Germany',2018,'F',2), 
('Germany',2018,'F',9),
)

print('\n_________health_index_2017_______________')

health_index_2017={
    country+'_'+str(health_index):[sex,health_index]
    for country,year,sex,health_index in a
    if year<=2017
    }
print(health_index_2017)
print('\n health_index_2017 has ' +str(len(health_index_2017))+' items')

#ex: health_index_2017 = {'France': [sex, health_index]}
print('\n_________ health_index_2018 _______________')

health_index_2018={
    country+'_'+str(health_index):[sex,health_index]
    for country,year,sex,health_index in a
    if year>2017
    }
print(health_index_2018)
print('\n health_index_2018 has ' +str(len(health_index_2018))+' items\n')

#one dict that groups all data by year for Germany
germany={
    country+'_'+str(sex)+'_'+str(health_index)+'_'+str(year):[sex,health_index]
    for country,year,sex,health_index in a
    if country=='Germany'
    }
print(germany)
print('\n Germany has ' +str(len(germany))+' items \n')

#one dict that grups all data by country and year, by using year in the key together with the country name
print('\n one dict "health_index_belgium" ,that grups all data by country and year, by using year in the key together with the country name\n')

health_index_belgium={
    country+'_'+str(sex)+'_'+str(health_index)+'_'+str(year):[year,sex,health_index]
    for country,year,sex,health_index in a
    if country=='Belgium'
    }
print(health_index_belgium)
print('\n health_index_belgium has ' +str(len(health_index_belgium))+' items')
#starting from the previous health_index dict, display only the data where the health_index > 5
print ('\n starting from the previous health_index dict, display only the data where the health_index > 5\n')
health_index_belgium={
    country+'_'+str(sex)+'_'+str(health_index)+'_'+str(year):[year,sex,health_index]
    for country,year,sex,health_index in a
    if country=='Belgium'and health_index>5
    }
print(health_index_belgium)
#starting from the previous health_index dict , display only the data where the health_index > 5 and sex is 'F'
print ("\n starting from the previous health_index dict, display only the data where the health_index > 5 and sex is 'F'\n")
health_index_belgium={
    country+'_'+str(sex)+'_'+str(health_index)+'_'+str(year):[year,sex,health_index]
    for country,year,sex,health_index in a
    if country=='Belgium'and health_index>5 and sex=='F'
    }
print(health_index_belgium)
#starting from the previous health_index dict, create a for loop to print the health_index
print ("\n starting from the previous health_index dict, create a for loop to print the health_index\n")
health_index_belgium={
    country+'_'+str(sex)+'_'+str(health_index)+'_'+str(year):[health_index]
    for country,year,sex,health_index in a
    if country=='Belgium'and health_index>5 and sex=='F'
   }
print (health_index_belgium.values())
