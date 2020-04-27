from collections.abc import MutableMapping, Mapping, Iterable, Collection, Container, Sized

class StudentsCollection(object):

    def __init__(self, students_list=None):
        self._students = list(students_list) if students_list else []

    def __iter__(self):
        return iter(self._students)

    def __getitem__(self, index):
        return self._students[index]

    def __contains__(self, element):
        return element in self._students
    
    def __len__(self):
        return len(self._students)

test = [1, 4, 6, 7]

stud_collection = StudentsCollection(test)

print(type(stud_collection))
print("__len__ test: {}".format(len(stud_collection)))
print("__contains__ test: {}".format(4 in stud_collection))

abcs = [MutableMapping, Mapping, Iterable, Collection, Container, Sized]
for abc in abcs:
    print(
        'stud_collection is a {}: {}'.format(
            abc.__name__, isinstance(stud_collection, abc))
    )