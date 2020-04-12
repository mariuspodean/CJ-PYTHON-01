# Build two classes of your choice that can model a real-life example. The class needs to meet the following
# requirements:
#
# - at least 5 attributes each
# - at least 2 methods each
# - one class to inherit from another
#
# As a demonstration create at least 5 instances of one class (preferably the child class) and call all the methods
# it holds
#
# Ex: You can have one class (Country) that has general attributes about countries such as area, neighbours,
# cities etc and methods related to those attributes. The second class can be a specific country (Romania) that has
# more specific attributes such as attractions, universities etc.

# add a comparison country
ref_country = ['Austria', 'Europe', 'Central Europe', '83879', '+43', 12, 8.85, 2.75, 34, 60]

# 83879 square kilometers
# 12 major cities
# 8.85 total population
# 2.75 population in major cities
# 34 universities
# 60 touristic attractions


class Country(object):
    def __init__(self, name, continent, position, area, code, major_cities,
                 population_country, populations_major_cities):
        self.name = name
        self.continent = continent
        self.position = position
        self.area = area
        self.code = code
        self.major_cities = major_cities
        self.population_country = population_country
        self.populations_major_cities = populations_major_cities

    def location(self):
        if self.continent is ref_country[1] and self.position is ref_country[2]:
            return f'Both, {ref_country[0]} and {self.name}, are on same continent ({self.continent}) ' \
                   f'and same area: {self.position}'
        elif self.continent is ref_country[1] and self.position is not ref_country[2]:
            return f'Both, {ref_country[0]} and {self.name}, are on same continent ({self.continent}) ' \
                   f'but on different areas: \n{ref_country[0]} is on {ref_country[2]} area ' \
                   f'and {self.name} is on {self.position} area'
        elif self.continent is not ref_country[1]:
            return f' {ref_country[0]}  and {self.name} are on different continents'

    def area_comparison(self):
        if int(self.area) == int(ref_country[3]):
            return f'Both, {ref_country[0]} and {self.name}, have same area: {self.area} square kilometers'
        elif int(self.area) > int(ref_country[3]):
            percentage = int(((int(self.area) - int(ref_country[3])) / int(self.area)) * 100)
            return f'{self.name} is bigger than {ref_country[0]} with {percentage} %'
        elif int(self.area) < int(ref_country[3]):
            percentage = int(((int(ref_country[3]) - int(self.area)) / int(ref_country[3])) * 100)
            return f'{ref_country[0]} is bigger than {self.name} with {percentage} %'


class Romania(Country):
    def __init__(self, name, continent, position, area, code, major_cities,
                 population_country, populations_major_cities, list_univ, attractions):
        self.list_univ = list_univ  # list of universities
        self.attractions = attractions  # attractions number
        super().__init__(name, continent, position, area, code, major_cities,
                         population_country, populations_major_cities)

    def country_code(self):
        return f'{self.name} has {self.code} and {ref_country[0]} has {ref_country[4]} country code'

    def percent_pop_cities(self):
        percentage_one = (ref_country[7] / ref_country[6]) * 100
        percentage_two = (self.populations_major_cities / self.population_country) * 100
        return f'{int(percentage_one)}% of {ref_country[0]}s %s population is living in major cities.' \
               f'\nSimilar {int(percentage_two)}% of {self.name}s population'

    def universities(self):
        return f'{ref_country[0]} has {ref_country[8]} universities at {ref_country[6]} millions of people and ' \
               f'\n{ref_country[9]} tourist attractions at {ref_country[3]} square kilometers. ' \
               f'\n{self.name} has {self.list_univ} universities at {self.population_country} millions of people ' \
               f'\nand {self.attractions} tourist attractions at {self.area} square kilometers'


romania = Country('Romania', 'Europe', 'Central Europe', '238397', '+40', 15, 20, 8)
print(romania.location())
print(romania.area_comparison())
print()
code = Romania('Romania', 'Europe', 'Central Europe', '238397', '+40', 15, 19.41, 6.4, 25, 80)
print(code.country_code())
comparison1 = Romania('Romania', 'Europe', 'Central Europe', '238397', '+40', 15, 19.41, 6.4, 53, 80)
print(comparison1.percent_pop_cities())
print()
comparison2 = Romania('Romania', 'Europe', 'Central Europe', '238397', '+40', 15, 19.41, 6.4, 53, 80)
print(comparison2.universities())
