class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age_check = age

    @property
    def age_check(self):
        return self.final_age

    @age_check.setter
    def age_check(self, age):
        if type(age) is not int:
            raise TypeError('Age must be integer')

        if age < 18:
            raise ValueError('Minimal age is 18')

        self.final_age = age

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.first_name,
            self.last_name, self.age_check, id(self)
        )

    def __str__(self):
        return '{} {}, {}'.format(
            self.first_name, self.last_name, self.age_check)

john = Student('Elton', 'John', 21)
print(john.age_check)
john.age_check = 22
print(john.age_check)
joe = Student('Joe', 'Dow', 30)
print(joe.age_check)
print(joe.final_age)
joe = Student('Joe', 'Dow', 15)
