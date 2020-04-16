class Employee(object):
    company = 'Ford COM'

    def __init__(self, first_name, last_name, age, studies, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.studies = studies
        self.grade = grade

    @classmethod
    def from_dict(cls, dictionary):
        first_name = dictionary['first_name']
        last_name = dictionary['last_name']
        age = dictionary['age']
        studies = dictionary['studies']
        grade = dictionary['grade']

        return cls(first_name, last_name, age, studies, grade)

    def description(self):
        return f'The employee {self.first_name} {self.last_name[0]}. age: {self.age}'

    def is_promoted(self):
        return self.grade > 7 and self.age <= 60

    def __repr__(self):
        return f'Employee: {self.first_name} {self.last_name} with id: {id(self)}'

    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name[0]}.'


class InstructedEmployee(Employee):
    def __init__(self, first_name, last_name, age, studies, grade, courses):
        super().__init__(first_name, last_name, age, studies, grade)
        self.courses = courses

    def is_enrolled(self, course):
        return course in self.courses

    def is_promoted(self):
        return self.grade > 8 and self.age <= 50

    @staticmethod
    def welcome_message():
        print('Welcome to classes!')


ion = Employee('Ion', 'Dumitru', 40, 'Elementary', 6.7)
ion.description()
print(ion.company)
ion.is_promoted()

ionut = InstructedEmployee('Ionut', 'Vasile', 34, 'Highschool', 8.1, ['Technical course'])
ionut.is_enrolled('Python')
ionut.is_enrolled('Technical course')
print(ionut.company)
ionut.description()
ionut.is_promoted()
ionut.welcome_message()
marian = Employee.from_dict({'first_name': 'Marian', 'last_name': 'Badea', 'age': 25, 'studies': 'College', 'grade': 9})
marian.description()
print(marian)  # Employee: Marian B.
marian.__str__()
marian.__repr__()  # <bound method Employee.__repr__ of Employee: Marian Badea with id: 58939728>
