"""Design a game class that includes two genres of games and if you can play single or multi-player.

The challenge must have the following criteria:

1.Create at least two attributes for the sub classes and a overload method.
2.You should be able to add revenues and compare two different genres and checkout score/rating by average/country.
3.Create a Mixin class that displays the score of each game in order to know if it is worth playing.

Solve the challenge"""

from pythonlangutil.overload import Overload, signature


class Game:
    """Available Genres: Indie, Shooter and Strategy all of which can be single and multi-player"""
    def __init__(self, name, genre, players):
        self.name = name
        self.genre = genre
        self.players = players

    def __str__(self):
        return f'The game {self.name} is part of the {self.genre} genre and is {self.players}'


class GamerScoreMixin:
    def is_it_worth_playing(self):
        if sum(self.score.values()) / len(self.score) == 100:
            disclaimer = f'The game {self.name} is a masterpiece, definitely play it'
        elif sum(self.score.values()) / len(self.score) > 50:
            disclaimer = f'The game {self.name} is mediocre, play it if you have time to kill'
        else:
            disclaimer = f'The game {self.name} is trash, do not touch it, even with a 10 feet pole'
        return disclaimer

    @Overload
    @signature()
    def get_rating(self):
        return sum(self.score.values()) / len(self.score)

    @get_rating.overload
    @signature('str')
    def get_rating(self, country):
        return self.score[country]

    def improved_get_rating(self, country=None):
        if country is None:
            return sum(self.score.values()) / len(self.score)
        else:
            return self.score[country]


class IndieGame(Game, GamerScoreMixin):

    def __init__(self, name, genre, players, score, revenue):
        super().__init__(name, genre, players)
        self.score = score
        self.revenue = revenue

    def __add__(self, other):
        return f'The game {self.name} and {other.name} have {self.revenue + other.revenue} combined revenue'

    def __eq__(self, other):
        return self.score == other.score


class ShooterGame(Game, GamerScoreMixin):
    def __init__(self, name, genre, players, score, revenue):
        super().__init__(name, genre, players)
        self.score = score
        self.revenue = revenue


class StrategyGame(Game, GamerScoreMixin):
    def __init__(self, name, genre, players, score, revenue):
        super().__init__(name, genre, players)
        self.score = score
        self.revenue = revenue


hollow_knight = IndieGame(name='Hollow Knight',
                          genre='Indie Game',
                          players='single-player',
                          score={"UK": 100, "Germany": 100, "Romania": 100},
                          revenue=1000000)
cs_go = ShooterGame(name='Counter-Strike: Global Offensive',
                    genre='Shooter Game',
                    players='multi-player',
                    score={"UK": 52, "Germany": 51, "Romania": 50},
                    revenue=414000000)
dota2 = StrategyGame(name='Dota 2',
                     genre='Strategy game',
                     players='multi-player',
                     score={"UK": 13, "Germany": 12, "Romania": 11},
                     revenue=406000000)

print(hollow_knight)
print(hollow_knight.is_it_worth_playing())
print(dota2)
print(dota2.is_it_worth_playing())
print(cs_go)
print(cs_go.is_it_worth_playing())
print(hollow_knight + dota2)
print(dota2 == cs_go)
print('Basic function', dota2.get_rating())
print('Overloaded function', dota2.get_rating('Romania'))
print('Best function', cs_go.improved_get_rating())
print('Best function', cs_go.improved_get_rating('UK'))
