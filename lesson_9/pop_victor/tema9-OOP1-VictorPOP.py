'''
Build two classes of your choice that can model a real-life example.
The class needs to meet the following requirements:

at least 5 attributes each
at least 2 methods each
one class to inherit from another
As a demonstration create at least 5 instances of one class (preferably the child class)
 and call all the methods it holds
'''
from datetime import datetime


class User(object):

    def __init__(self, nickname, real_name, age, country, join_year):
        self.nickname = nickname
        self.real_name = real_name
        self.age = age
        self.country = country
        self.join_year = join_year

    def __repr__(self):
        return f'Nick: {self.nickname} age: {self.age} from: {self.country}'

    def __str__(self):
        return f'{self.nickname} joined in {self.join_year}'

    def account_age(self):
        return datetime.now().year-self.join_year

    def account_restriction(self):
        company_country = ['Romania', 'Luxembourg', 'Austria', 'Germany']
        if self.country in company_country:
            return f'{self.nickname} has access to {self.country} Server'
        return f'no server in {self.country} at the moment, sorry {self.nickname}'


class Gamer(User):
    def __init__(self, nickname, real_name, age, country, join_year, *args):
        self.games = args
        super().__init__(nickname, real_name, age, country, join_year)

    def number_games(self):
        return len(self.games)

    def list_games(self):
        print(f'{self.nickname} plays :')
        return ' - '.join(game for game in self.games)

    def blizz_games(self):
        list_games = ['wow', 'sc', 'sc2', 'diablo', 'hs']
        return len([game for game in self.games if game.lower() in list_games])


j0ke = Gamer('j0ke', 'Victor', 34, 'Romania', 2000, 'WoW', 'SC2', 'CS')
print(j0ke)
print(j0ke.account_age())
print(j0ke.account_restriction())
print(j0ke.number_games())
print(j0ke.list_games())
print(j0ke.blizz_games())

input_data = [
    ('j0ke', 'Victor', 34, 'Romania', 2000, 'WoW', 'SC2', 'CS'),
    ('Spionu', 'Lau', 20, 'Austria', 2012, 'CS', 'SC'),
    ('Oli', 'Olimpiu', 17, 'United States', 2017, 'CS'),
    ('rdu', 'Radu', 40, 'United Kingdom', 1997, 'SC', 'SC2', 'CS'),
    ('lipo', 'Cristi', 69, 'Luxembourg', 1990, 'Wow')
]
print(str(input_data[0]).strip(")("))

gamer_list = [
    Gamer(nickname, real_name, age, country, join_year, *args)
    for nickname, real_name, age, country, join_year, *args in input_data
]
print(f'\n{len(gamer_list)} - gamers registed\n')

for each_gamer in gamer_list:
    print(each_gamer)
    print(f'{each_gamer.account_age()} years old account')
    print(each_gamer.account_restriction())
    print(f'from a total of {each_gamer.number_games()} games')
    print(each_gamer.list_games())
    print(f'{each_gamer.blizz_games()} games are played on our SERVER')
    print()
