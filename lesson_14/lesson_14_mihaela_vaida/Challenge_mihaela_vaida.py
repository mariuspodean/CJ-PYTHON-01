class Movie:
    def __init__(self, name, director, release_year):
        self.name = name
        self.director = director
        self.release_year = release_year
        if type(release_year) != int or release_year < 1900:
            raise Exception('Not a correct release year !')

    def __str__(self):
        return f' The movie {self.name}, directed by {self.director} was released in {self.release_year}. '


class ImdbRateMixin:
    def how_is_theimdb_rating(self):
        if self.imdb_rate > 5:
            message = f'The movie {self.name} has a  good IMDB  score {self.imdb_rate}!'
        else:
            message = f'The movie {self.name} has a  bad IMDB  score {self.imdb_rate}!'
        return message


class Series(Movie, ImdbRateMixin):

    def __init__(self, name, director, release_year, imdb_rate, income):
        super().__init__(name, director, release_year)

        self.imdb_rate = imdb_rate
        self.income = income
        if type(self.income) != int and self.income < 0:
            raise Exception('Not a proper movie!')
        if type(self.imdb_rate) != int and self.imdb_rate <= 0:
            raise Exception('Only positive integers are allowed for IMDB rate!')

    # add money from 2 movies
    def __add__(self, other):
        return f' Money from the movies {self.name} and {other.name} are {self.income + other.income}'

    def __radd__(self, other):
        return f' Money from the movies {other.name} and {self.name} are {other.income + self.income}'

    # compare incomes from 2 movies
    def __eq__(self, other):
        return self.income == other.income


class ArtisticMovie(Movie, ImdbRateMixin):
    def __init__(self, name, director, release_year, imdb_rate, income):
        super().__init__(name, director, release_year)
        self.imdb_rate = imdb_rate
        self.income = income


titanic = ArtisticMovie('Titanic', 'James Cameron', 1997, 7.8, 2208208395)
friends = Series('Friends', 'David Crane, Marta Kauffman', 1994, 8.9, 2000000000)
titanic == friends  # False
friends == titanic  # False
tit = Series('Friends', 'David Crane, Marta Kauffman', 1994, 8.9, 2208208395)
tit == titanic  # True
titanic + friends  # ' Money from the movies Titanic and Friends are 4208208395'
friends + titanic  # ' Money from the movies Friends and Titanic are 4208208395'
print(titanic)
print(friends)
