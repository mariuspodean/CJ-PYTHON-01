'''Challenge
Implement a context manager called just_some_exceptions that will handle KeyError, IndexError by printing a message and
let any other exceptions propagate outside of the context manager.

Implement the context manager by using both approaches: by using class and by using @contextmanager

Write examples that prove the functionality for all the handled exceptions and for one exception that is not handled.'''
import contextlib


@contextlib.contextmanager
def some_exceptions(context):
    try:
        yield context
    except KeyError:
        print(f'ContextLib => Invalid key: {context}')
    except IndexError:
        print(f'ContextLib => Invalid index: {context}')


with some_exceptions('Some invalid key'):
    raise KeyError

with some_exceptions(-1):
    raise IndexError


class SomeException:

    def __enter__(self):
        print('Entering the exception manager..')

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is IndexError:
            print(f'Class => Invalid index: {exc_value}', traceback)
            handled = True
        elif exc_type is KeyError:
            print(f'Class => Invalid key: {exc_value}', traceback)
            handled = True
        else:
            handled = False
        print('Exiting the exception manager..')
        return handled


with SomeException():
    person = {'name':'Cristian', 'title':'Mare Baiat'}
    print(person['age'])

with SomeException():
    array = [1, 'ceva']
    print(array[2])

with SomeException():
    print(2/0)
