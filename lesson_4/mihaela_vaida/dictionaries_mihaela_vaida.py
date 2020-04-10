import pprint

#Dictionaries homework
#Using data from Eurostat, create a list of tuples representing the “Self-perceived health by
#country and sex, age group >16, for people living in cities” for 2017-2018. Have at least
#30 values in your dataset.
#The dataset will have the following struncture: > [ > (country, year, sex, health_index) > ]
#Example: > [(‘France’, 2017, M, 12), …]
#Using only comprehensions, create the following dicts: - two dicts that group all data by country
#for each year > health_index_2017 = {‘France’: [sex, health_index]} > health_index_2017 =
#{‘France’: [sex, health_index]}
#- one dict that groups all data by year for Germany > germany =
#{2017: [sex, health_index]}
#- one dict that grups all data by country and year, by using year in the
#key together with the country name > health_index = {‘France_2017’: [year, sex, health_index]}
#- starting from the previous health_index dict, display only the data where the health_index >
#5 - starting from the previous health_index dict, display only the data where the health_index
#> 5 and sex is ‘F’ - starting from the previous health_index dict, create a for loop to print the
#health_index"""


pretty_printer=pprint.PrettyPrinter(indent=4)

countries_F=['Estonia_F',
'Ireland_F',
'Greece_F',
'Spain_F',
'France_F',
'Croatia_F',
'Italy_F',
'Cyprus_F',
'Latvia_F',
'Lithuania_F',
'Luxembourg_F',
'Hungary_F',
'Malta_F',
'Netherlands_F',
'Austria_F',
'Poland_F',
'Portugal_F',
'Romania_F',
'Slovenia_F',
'Slovakia_F',
'Finland_F',
'Sweden_F',
'United Kingdom_F',
'Iceland_F',
'Norway_F',
'Switzerland_F',
'Montenegro_F',
'North Macedonia_F',
'Serbia_F',
'Turkey_F'
]

countries_M=['Estonia_M',
'Ireland_M',
'Greece_M',
'Spain_M',
'France_M',
'Croatia_M',
'Italy_M',
'Cyprus_M',
'Latvia_M',
'Lithuania_M',
'Luxembourg_M',
'Hungary_M',
'Malta_M',
'Netherlands_M',
'Austria_M',
'Poland_M',
'Portugal_M',
'Romania_M',
'Slovenia_M',
'Slovakia_M',
'Finland_M',
'Sweden_M',
'United Kingdom_M',
'Iceland_M',
'Norway_M',
'Switzerland_M',
'Montenegro_M',
'North Macedonia_M',
'Serbia_M',
'Turkey_M']
len(countries_F)   #30
len(countries_M)   #30

h_index_2017_M=[10.6,
44.5,
47.4,
20.5,
26.3,
30.8,
15.1,
50.5,
4.3,
9.1,
24.9,
20.4,
30.6,
24.6,
33.5,
18.4,
12.2,
31.5,
23.8,
25.7,
20.2,
30.2,
37.0,
':',
27.9,
37.5,
44.0,
29.6,
21.0,
6.6]

h_index_2018_M=[9.3,
45.7,
48.1,
24.1,
24.3,
31.2,
16.4,
47.9,
6.8,
9.0,
23.8,
18.5,
26.3,
26.9,
32.8,
16.9,
11.0,
30.2,
23.1,
24.4,
19.4,
31.7,
34.0,
':',
28.8,
36.8,
':',
31.2,
22.6,
':']

h_index_2017_F=[
11.3,
44.8,
42.8,
17.7,
22.4,
25.5,
12.2,
48.7,
2.8,
6.2,
22.1,
14.1,
26.4,
20.1,
31.7,
14.5,
8.9,
24.4,
19.0,
20.9,
19.2,
27.7,
33.8,
':',
28.5,
32.6,
35.8,
25.0,
16.1,
4.5]
h_index_2018_F=[
8.4,
45.5,
44.1,
21.1,
21.7,
26.2,
13.6,
45.3,
4.4,
5.7,
23.3,
14.1,
22.5,
20.2,
31.1,
14.2,
8.6,
22.9,
17.2,
20.1,
16.5,
26.7,
32.5,
':',
27.4,
33.7,
':',
27.2,
19.5,
':']
#Using only comprehensions, create the following dicts:

#two dicts that group all data by country for each year

#from collections.abs import Iterable


first_iterable_F = zip(countries_F, h_index_2017_F)
second_iterable_F = zip(countries_F, h_index_2018_F)
first_iterable_M = zip(countries_F, h_index_2017_M)
second_iterable_M = zip(countries_F, h_index_2018_M)
health_index_F_2017=dict(first_iterable_F)
health_index_F_2018=dict(second_iterable_F)
health_index_M_2017=dict(first_iterable_M)
health_index_M_2018=dict(second_iterable_M)

countries=countries_F+countries_M

h_index_2017=h_index_2017_F+h_index_2017_M
h_index_2018=h_index_2018_F+h_index_2018_M
first_iterable=zip(countries,h_index_2017)
second_iterable=zip(countries,h_index_2018)
health_index_2017=dict(first_iterable)
health_index_2018=dict(second_iterable)

#print(health_index_2017)
#print(health_index_2018)

#----------------- or :

#two dicts that group all data by country  for each year 
H_2017=list(zip(countries, h_index_2017))
H_2018=list(zip(countries, h_index_2018))


H_2017_dict={country:h_index for country,h_index in H_2017}
H_2017_dict
H_2018_dict={country:h_index for country,h_index in H_2018}
H_2018_dict

# one dict that groups all data by year for Germany > germany = {2017: [sex, health_index]}
HI_F2017=[(2017,'F', h_index) for h_index in h_index_2017_F ]
HI_F2018=[(2018,'F', h_index) for h_index in h_index_2018_F ]
HI_M2017=[(2017,'M', h_index) for h_index in h_index_2017_M ]         
HI_M2018=[(2018,'M', h_index) for h_index in h_index_2018_M ]
###
H_F_=list(zip(countries, HI_F2017+HI_F2018))
H_M_=list(zip(countries, HI_M2017+HI_M2018))
#o alta varianta pt prima cerinta 
#dict1 Healt_index pt femei, in 2017 si 2018 , dict- numai pt barbati in ambii ani
dict1=dict(H_F_)
dict2=dict(H_M_)

#

dict1['Germany_F']=('2017', 'F', 10.5)
dict1['Germany_M']=('2017_', 'M', 9.9)      
dict2['Germany_F']=('2018', 'F', 10.6)
dict2['Germany_M']=('2018_', 'M', 8.9)
print(dict1.get('Germany_F', 'Not found'))
print(dict1.get('Germany_M', 'Not found'))      
print(dict2.get('Germany_F', 'Not found'))
print(dict2.get('Germany_M', 'Not found'))


GermanyF= dict1['Germany_F']
GermanyM=dict1['Germany_M']
Germanyf=dict2['Germany_F']
Germanym=dict2['Germany_M']
Germany=[GermanyF,GermanyM,Germanyf, Germanym]
#-------------------------------------
#One Dictionary that groups all data for Germany

Germany_dict={year:(sex, H_index) for year, sex , H_index in Germany}

#---------------------------
#one dictionary that groups all data by country and year ( am facut numai pt cele 30 de state  ,femei, 2017)
countries_F_2017=['Estonia_F_2017',
'Ireland_F__2017',
'Greece_F_2017',
'Spain_F_2017',
'France_F_2017',
'Croatia_F_2017',
'Italy_F_2017',
'Cyprus_F_2017',
'Latvia_F_2017',
'Lithuania_F_2017',
'Luxembourg_F_2017',
'Hungary_F_2017',
'Malta_F_2017',
'Netherlands_F_2017',
'Austria_F_2017',
'Poland_F_2017',
'Portugal_F_2017',
'Romania_F_2017',
'Slovenia_F_2017',
'Slovakia_F_2017',
'Finland_F_2017',
'Sweden_F_2017',
'United Kingdom_F_2017',
'Iceland_F_2017',
'Norway_F_2017',
'Switzerland_F_2017',
'Montenegro_F_2017',
'North Macedonia_F_2017',
'Serbia_F_2017',
'Turkey_F_2017'
]

H_IndexF2017=[(2017,'F',H_index) for H_index in h_index_2017_F]
H_index_F2017=list(zip(countries_F_2017,H_IndexF2017))
dict(H_index_F2017)
H_I_dict2017_F={country:[iteration] for country, iteration in H_index_F2017 }


#starting for the previous health index dict, display only the data  where  the Health index>5


Dict={country: tuple for country , tuple in H_index_F2017 if type(tuple[2])!=str and tuple[2]>5 }



#starting for the previous health index dict, display only the data  where  the Health index>5 and  sex is 'F ' ( in lista mea de mai sus am numai F)


Dict_={country: tup for country , tup in H_index_F2017 if type(tup[2])!=str and tup[2]>5  and tup[1]=='F'}


#H_IndexF2017_={country:[iteration] for country, iteration in H_index_F2017  for _,sex ,_ in iteration if sex=='F'}

#starting from the previous health_index dict, create a for loop to print the health_index


for country, infos in H_I_dict2017_F.items() :

    print('{} - {}'.format(country, infos) )





