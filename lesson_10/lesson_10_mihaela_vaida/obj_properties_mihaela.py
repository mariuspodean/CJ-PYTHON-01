class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name

        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if type(age) is not int:
            raise TypeError('Age must be integer')

        if age < 18:
            raise ValueError('Minimal age is 18')

        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.first_name,
            self.last_name, self.age, id(self)
        )

    def __str__(self):
        return '{} {}, {}'.format(
            self.first_name, self.last_name, self.age)


john = Student('Elton', 'John', 21)

Ana = Student('Ana', 'Maria', 15)  # Traceback (most recent call last):ValueError: Minimal age is 18
Anna = Student('Ana', 'Maria', 'ewew')  # TypeError: Age must be integer
