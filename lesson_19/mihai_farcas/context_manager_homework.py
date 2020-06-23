"""
Challenge Implement a context manager called just_some_exceptions
that will handle KeyError, IndexError by printing a message and let
 any other exceptions propagate outside of the context manager.

Implement the context manager by using both approaches: by using class and by using @contextmanager

Write examples that prove the functionality for all the handled exceptions and for one exception that is not handled.
# except: (FileNotFoundError,"Not found")
"""
from contextlib import contextmanager

@contextmanager
def some_function():
    try:
        # KeyError: 'four'
        a_dict = {
            "one": "1",
            "two": "2",
            "tree":"3"
        }

        a_dict["four"]
    except KeyError:
        print("Key not found, please enter a valid one\n")

    # IndexError: list index out of range
    try:
        a_list = [1, 2, 3, 4, 5, 6]
        print(a_list[10])
    except IndexError:
        print("Please select another index, this is out of range \n")


try:
    open("a.txt", "r")
    a = 10 / 0

except FileNotFoundError:
    print("Please enter a valid file name , filename provided is not found\n ")
except ZeroDivisionError:
    print("Not a valid operation, division by 0 ")




