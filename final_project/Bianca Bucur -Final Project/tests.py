from application import *
from playground import *
import unittest

class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Start Testing! :)')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing! :(')

    def test_person_init(self):
        Person1 = Person(1, "Bucur", "Bianca", 20, "Student")
        self.assertIsInstance(Person1, Person)

    def test_person_attributes(self):
        index = 1
        surname = 'Bucur'
        name = 'Bianca'
        age = 20
        status = 'Student'
        Person1 = Person(index, surname, name, age, status)
        assert hasattr(Person1, 'index'), "This person's index is missing !"
        assert hasattr(Person1, 'surname'), "This person's surname is missing !"
        assert hasattr(Person1, 'name'), "This person's name is missing !"
        assert hasattr(Person1, 'age'), "This person's age is missing !"
        assert hasattr(Person1, 'status'), "This person's status is missing !"

class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Start Testing! :)')

    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing! :(')

    def test_student_init(self):
        Student3 = Student(6, "Zeni", "Luca", 18, "Student")
        self.assertIsInstance(Student3, Student)

    def test_student_attributes(self):
        index = 6
        surname = 'Zeni'
        name = 'Luca'
        age = 18
        status = 'Student'
        Student3 = Student(index, surname, name, age, status)
        assert hasattr(Student3, 'index'), "This student's index is missing !"
        assert hasattr(Student3, 'surname'), "This student's surname is missing !"
        assert hasattr(Student3, 'name'), "This student's name is missing !"
        assert hasattr(Student3, 'age'), "This student's age is missing !"
        assert hasattr(Student3, 'status'), "This student's status is missing !"


class TestTeacher(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        print('Start Testing! :)')


    @classmethod
    def tearDownClass(cls) -> None:
        print('End Testing! :(')


    def test_teacher_init(self):
        Teacher2 = Teacher(4, "Spinieli", "Angelica", 40, "Teacher")
        self.assertIsInstance(Teacher2, Teacher)


    def test_student_attributes(self):
        index = 4
        surname = 'Spinieli'
        name = 'Angelica'
        age = 40
        status = 'Teacher'
        Teacher2 = Student(index, surname, name, age, status)
        assert hasattr(Teacher2, 'index'), "This teacher's index is missing !"
        assert hasattr(Teacher2, 'surname'), "This teacher's surname is missing !"
        assert hasattr(Teacher2, 'name'), "This teacher's name is missing !"
        assert hasattr(Teacher2, 'age'), "This teacher's age is missing !"
        assert hasattr(Teacher2, 'status'), "This teacher's status is missing !"
