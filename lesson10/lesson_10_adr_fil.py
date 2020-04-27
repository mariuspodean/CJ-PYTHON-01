
class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.varsta_student = age

    @property
    def varsta_student(self):
        print('Getter')
        return self._varsta

    @varsta_student.setter
    def varsta_student(self, varsta):
        print('Setter')
        if type(varsta) is not int:
            raise TypeError('Age must be integer')
        if varsta < 18:
            raise ValueError('Minimal age is 18')
        self._varsta = varsta

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.first_name,
            self.last_name, self.varsta_student, id(self)
        )

    def __str__(self):
        return '{} {}, {}'.format(
            self.first_name, self.last_name, self.varsta_student)


john = Student('Elton', 'John', 21)
john.varsta_student

john.varsta_student = 22
# ValueError: Minimal age is 18
joe = Student('Joe', 'Dow', 19)
