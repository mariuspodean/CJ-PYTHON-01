class Movies(object):

    def __init__(self, country_origin, movie_name, year_released, director, stars):
        self.country = country_origin
        self.movie = movie_name
        self.year = year_released
        self.director = director
        self.stars = stars

    def get_name_year(self):
        return f"Movie for {self.country} from year {self.year}: {self.movie}"

    def get_name_stars(self):
        return f"Starring in the movie {self.movie} are: {self.stars}"

    def by_year(self):
        if self.year > 2000:
            print(f"These {self.movie} were release after year 2000")


class Romania(Movies):

    def __init__(self, country_origin, movie_name, year_released, director, stars, synopsis):
        super().__init__(country_origin, movie_name, year_released, director, stars)

        self.plot = synopsis

    def directed_by(self):
        return f"Movies from {self.country} directed by {self.director} are: {self.movie}"

    def synopsis(self):
        return f"The plot for {self.movie} is: \"{self.plot}\"."


orig_RO = Movies("Romania", "America venim!", 2014, "Razvan Savescu", ("Alina Berzunteanu", "Alexandru Bindea"))
orig_DE = Movies("Germany", "A coffee in Berlin", 2012, "Jan Ole Gerster", ("Tom Schilling", "Friederike Kempter"))
orig_FR = Movies("France", "The Intouchables", 2011, "Olivier Nakache", ("François Cluzet", "Omar Sy"))
orig_AM = Movies("America", "Pulp Fiction", 1994, "Quentin Tarantino", ("Samuel L. Jackson", "Uma Thurman"))
orig_JP = Movies("Japan", "Seven Samurai", 1954, "Akira Kurosawa", ("Toshirô Mifune", "Takashi Shimura"))
ro = Romania("Romania", "America venim!", 2014, "Razvan Savescu", ("Alina Berzunteanu", "Alexandru Bindea"),
             "Six Romanian artists get to live the dream of their life in a road-movie full of adventures:"
             " America, here we come!")

print(Movies.get_name_year(orig_AM))
print(Movies.get_name_year(orig_JP))
print(orig_FR.get_name_stars())
print(orig_DE.get_name_stars())
print(ro.directed_by())
print(ro.synopsis())
