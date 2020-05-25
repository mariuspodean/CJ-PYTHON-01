# Challenge
# Implement a context manager called just_some_exceptions that will handle KeyError, IndexError by printing a message
# and let any other exceptions propagate outside of the context manager.
# Implement the context manager by using both approaches: by using class and by using @contextmanager
# Write examples that prove the functionality for all the handled exceptions and for one exception that is not handled.

import contextlib

letters = ('a', 'b', 'c', 'd')
numbers = (1, 2, 3, 4)
dictionary = dict(zip(letters, numbers))

@contextlib.contextmanager
def just_some_exceptions():

    try:
        yield "generator"
    except (KeyError, IndexError):
        print("Exception handling message")


with just_some_exceptions() as smth:
    print(dictionary['x'])
    print(smth)

with just_some_exceptions() as smth:
    print(letters[5])
    print(smth)

with just_some_exceptions() as smth:
    print(dictionary['a'])
    print(smth)

# error propagated outside the context manager
with just_some_exceptions() as smth:
    print(smth)
    print(abc)

class JustSomeExceptions:

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is KeyError or exc_type is IndexError:
            print("Exception handling message")
            test = True
        else:
            test = False
        return test

with JustSomeExceptions() as smth:
    print(dictionary['x'])
    print(smth)

with JustSomeExceptions() as smth:
    print(letters[5])
    print(smth)

# error propagated outside the context manager
with JustSomeExceptions() as smth:
    print(abcd)
    print(smth)