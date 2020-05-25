# simplify lesson_9


class Country(object):

    def __init__(self, name, continent, position, area):
        self.name = name
        self.continent = continent
        self.position = position
        self.area = area

    def continent_ver(self):
        if self.continent == 'Europe':
            return 'Same continent'
        else:
            return 'Different continent'

    def continent_ver_2(self):
        if self.continent == 'Europe':
            return 'Same continent'
        else:
            return 'Different continent'

    def continent_ver_3(self):
        if self.continent == 'Europe':
            return True
        else:
            return False

    def continent_ver_4(self):
        if self.continent == 'Europe':
            return True
        else:
            return False


# country1 = Country('Romania', 'Europe', 'Central Europe', '160000')
# print(country1.continent)
