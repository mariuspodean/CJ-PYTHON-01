import random
import logging

from contextlib import contextmanager
import pprint

pp = pprint.PrettyPrinter(indent=4)
logger = logging.getLogger(__name__)

__header__ = r'''
                _
              _|=|__________
             /              \
            /   HIGH SCHOOL  \
           /__________________\
            ||  || /--\ ||  ||
            ||[]|| | .| ||[]||
          ()||__||_|__|_||__||()
         ( )|-|-|-|====|-|-|-|( ) 
         ^^^^^^^^^^====^^^^^^^^^^^
.------------------------------------------.
| .--------------------------------------. |
| |                Info:                 | |
| |                                      | |
| |                                      | |
'''
__footer__ = r'''

| |                                      | |
| |                                      | |
| |                                      | |
| |______________________________________| |
|__________________________________________|
'''

class DisplayMixin:



#creating the class Person
class Person(DisplayMixin):
    def __init__(self, index, surname, name, age, status):
        self.surname = surname
        self.name = name
        self.age = age
        self.status = status

    def validate_person(self):

        error_msg = ""
        if self.surname is None:
            error_msg += "This person should have a surname "
        if self.name is None:
            error_msg += "This person should have a name "
        if self.age is None:
            error_msg += "This person should have an age "
        if self.status is None:
            error_msg += "This person should have a status "
        return True

    def contents(self):
        return self.surname.items()

    def __str__(self):
        return self.order_display()

    def __iter__(self):
        yield from iter(self.surname.items())

    def __getitem__(self, item):
     return self.surname[item]

    def __repr__(self):
        return self.surname + self.name

class Student(Person):
    def __init__(self, index, surname, name, age, status):
        super().__init__(index, surname, name, age, status)

    def validate_student(self):

        error_msg = ""
        if self.surname is None:
            error_msg += "This student should have a surname "
        if self.name is None:
            error_msg += "This student should have a name "
        if self.age is None:
            error_msg += "This student should have an age "
        return True

class Teacher(Person):
    def __init__(self, index, surname, name, age, status):
        super().__init__(index, surname, name, age, status)

    def validate_teacher(self):

        error_msg = ""
        if self.surname is None:
            error_msg += "This teacher should have a surname "
        if self.name is None:
            error_msg += "This teacher should have a name "
        if self.age is None:
            error_msg += "This teacher should have an age "
        return True

#class PersonFunctions:

   # def create_person(self, surname, name, age, status):

      #  def check_person
 #"  ███████╗██████╗ ██████╗  ██████╗ ██████╗"
  # "██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗"
   #"█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝"
   #"██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗"
   #"███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║"
   #"╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝"
    #" !! no person found with this surname !!"





