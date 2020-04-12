class Movies:

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


orig_RO = Movies("Romania", "America venim!", 2014, "Razvan Savescu", ("Alina Berzunteanu", "Alexandru Bindea"))
orig_DE = Movies("Germany", "A coffee in Berlin", 2012, "Jan Ole Gerster", ("Tom Schilling", "Friederike Kempter"))
orig_FR = Movies("France", "The Intouchables", 2011, "Olivier Nakache", ("François Cluzet", "Omar Sy"))
orig_AM = Movies("America", "Pulp Fiction", 1994, "Quentin Tarantino", ("Samuel L. Jackson", "Uma Thurman"))
orig_JP = Movies("Japan", "Seven Samurai", 1954, "Akira Kurosawa", ("Toshirô Mifune", "Takashi Shimura"))


print(Movies.get_name_year(orig_AM))
print(orig_FR.get_name_stars())


# movies_objects = []
# for movie in movies:
#     movies_objects.append(
#         Movies(
#             movie["country"],
#             movie["name"],
#             movie["year"],
#             movie["director"],
#             movie["stars"]
#         )
#     )


