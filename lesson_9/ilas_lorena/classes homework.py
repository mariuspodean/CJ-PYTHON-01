# Build two classes of your choice that can model a real-life example. The class needs to meet the following
# requirements:
# at least 5 attributes each at least 2 methods each one class to inherit from another As a demonstration create at
# least 5 instances of one class (preferably the child class) and call all the methods it holds


class Animal(object):

    def __init__(self, animal, name, n_legs, gender, speech_type):
        self.animal = animal
        self.name = name
        self.n_legs = n_legs
        self.gender = gender
        self.speech_type = speech_type

    def check_speech_type(self):
        if self.speech_type == 'meow':
            return 'It is a cat!'
        else:
            return f'{self.name} is a {self.animal} so it does not speak meow'

    def check_motility(self):
        if self.n_legs == 4:
            return f'{self.name} the {self.animal} has 4 legs so he can walk'
        elif self.n_legs == 0:
            return f'{self.name} the {self.animal} has no legs so it slides'
        else:
            return f'{self.name} has {self.n_legs} legs so maybe it jumps maybe it flies who knows'


class Dog(Animal):

    def __init__(self, animal, name, n_legs, gender, speech_type, breed, age):
        self.breed = breed
        self.age = age
        super().__init__(animal, name, n_legs, gender, speech_type)

    def check_breed(self):
        if self.breed[0:1] in ('B', 'G' ,'L', 'C'):
            return f'{self.name} is a {self.breed}'
        else:
            return 'unknown breed'

    def is_rescue_dog(self):
        if self.breed == 'German Shepherd':
            return f'{self.name} is a {self.breed} hence it is rescue dog'
        else:
            return f'{self.name} is a {self.breed} hence it is not a rescue dog'

    def check_age(self):
        if self.age <= 5:
            return f'{self.name} is a young dog'
        else:
            return f'{self.name} is an old dog'


Toby = Dog('dog', 'Toby', 4, 'M', 'bau', 'Beagle', 10)
Grace = Dog('dog', 'Grace', 4, 'F', 'bau', 'German Shepherd', 5)
Teddy = Dog('dog', 'Teddy', 4, 'M', 'bau', 'German Shepherd', 4)
Sandy = Dog('dog', 'Sandy', 4, 'F', 'bau', 'Labrador', 15)
Lola = Dog('dog', 'Lola', 4, 'M', 'bau', 'Chihuahua', 1)

print(Toby.check_breed())
print(Teddy.check_breed())
print(Sandy.check_breed())
print(Lola.check_breed())
print(Toby.is_rescue_dog())
print(Grace.is_rescue_dog())
print(Sandy.check_age())
print(Lola.check_age())

sandra = Animal('snake', 'Sandra', 0, 'F', 'hiss')
print(sandra.check_motility())
print(sandra.check_speech_type())

bobby = Animal('Kangaroo', 'Bobby', 2, 'M', 'screams')
print(bobby.check_motility())
print(bobby.check_speech_type())
