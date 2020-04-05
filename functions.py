description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
    '2019 '])
raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
]
countries = {
    "AL" : "Albania" , 
    "AT" : "Austria" , 
    'BA' : 'Bosnia and Herzegovina' , 
    'BE' : 'Belgium' , 
    'BG' : 'Bulgaria'
    }
result = {
    'Romania': [
                {'year': '2019', 'coverage': 84},
                {'year': '2018', 'coverage': 67},
    ],
    'Germany': [
                {'year': '2019', 'coverage': 84},
                {'year': '2018', 'coverage': 67},
    ],
}
years_clear = [
        int(elem.strip(' '))
        for elem in description[1]
    ]
print('Clear years are: YEARS_CLEAR')
print(years_clear)

#gasim lista coresponzatoare tarii raw_data[(tara[lista_cu_cov._data_points])]
def get_coverage_cc(cc):
    for row in raw_data:
        if cc in row:
            return(row[1])
print(get_coverage_cc('BE'))



def get_index_country(cc):
    for row in raw_data:
        if cc in row:
            return(raw_data.index(row))

def get_index_year(yy):
    for yyyy in description[1]:
            return(description[1].index(yyyy))


print(get_index_country('BE'))
print(get_index_year('2001 '))
#cov_clear = {
#    cc : [
#        {
#            'year' : years_clear[get_index_country(cc)] ,
#            'coverage':
#            for indexu in rage(len(years_clear))
#        }
#
#}