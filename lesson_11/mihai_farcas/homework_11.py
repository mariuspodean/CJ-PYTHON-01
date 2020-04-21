# Lesson 11 - Interfaces and protocols
from collections.abc import MutableMapping, Mapping, Iterable, Collection, Container, Sized


class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.first_name,
            self.last_name, self.age, id(self)
        )

    def __str__(self):
        return '{} {}, {}'.format(
            self.first_name, self.last_name, self.age)


class StudentsCollection:

    def __init__(self, students_list=None):
        self._students = list(students_list) if students_list else []

    def __iter__(self):
        return iter(self._students)

    def __getitem__(self, index):
        return self._students[index]

# define __len__ function for class StudentsCollection
    def __len__(self):
        return len(self._students)

# define __contains__ function for class StudentsCollection
    def __contains__(self, item):
        return item in self._students


# students = [
#     Student('John', 'Doe', 19),
#     Student('Jack', 'Fluffy', 18),
#     Student('Matthew', 'Wu', 19),
#     Student('Heather', 'Rafferty', 19),
#     Student('Randall', 'Blackdall', 20),
#     Student('Marissa', 'Raynaud', 19),
#     Student('Marlo', 'Ranbot', 19)
# ]
students =["Maria","George","Marian"]
stud_collection = StudentsCollection(students)

print(type(stud_collection))

abcs = [MutableMapping, Mapping, Iterable, Collection, Container, Sized]
for abc in abcs:
    print(
        'stud_collection is a {}: {}'.format(
            abc.__name__, isinstance(stud_collection, abc))
    )

#Make **StudentsCollection** a ***sized collection***.
print(len(students))
# stud_collection()
print("George" in stud_collection)