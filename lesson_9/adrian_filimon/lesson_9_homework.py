# Build two classes of your choice that can model a real-life example.
# The class needs to meet the following requirements:
# at least 5 attributes each
# at least 2 methods each
# one class to inherit from another
# As a demonstration create at least 5 instances of one class (preferably the child class)
# and call all the methods it holds

class Actors:
    def __init__(self, name, sex, age, notoriety, awards):
        self.full_name = name
        self.sex = sex
        self.age = age
        self.notoriety = notoriety
        self.awards = awards

    def best_known_villan(self):
        return f'The {self.sex} actor {self.full_name} at {self.age} age has won his notoriety with' \
               f' {self.notoriety} for which he won an {self.awards}.'

    def actors_over_80_years(self):
        if self.age > 80:
            return f'One of the most famous {self.sex} actors who is passed their 80s is {self.full_name}. ' \
                   f'Currently at {self.age} he is most famous for {self.notoriety} which won him an {self.awards}.'


class NonOscarWinners(Actors):
    def __init__(self, name, sex, age, notoriety, awards, fun_facts):
        super().__init__(name, sex, age, notoriety, awards)

        self.funfacts = fun_facts

    def funny_story(self, funfact):
        return funfact in self.funfacts


thonny = Actors('Anthony Hopkins', 'male', 82, 'The Silence of the Lambs', 'Oscar')

jacky = Actors('Jack Nicholson', 'male', 82, 'One Flew Over the Cuckoo`s Nest', 'Oscar')

morpheus = Actors('Lawrence Fishburne', 'male', 58, 'Matrix', 'no Oscars', 'was a junky')

print(thonny.best_known_villan())
print(jacky.actors_over_80_years())
print(morpheus.funny_story )