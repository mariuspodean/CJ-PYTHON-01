from contextlib import contextmanager

"""
Implement a context manager called just_some_exceptions that will handle KeyError, IndexError 
by printing a message and let any other exceptions propagate outside of the context manager.

Implement the context manager by using both approaches: by using class and by using @contextmanager

Write examples that prove the functionality for all the handled exceptions and for one exception that 
is not handled.
"""



class JustSomeExceptions:

    def __enter__(self):

        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is IndexError:
            print('This is the IndexError')
        elif exc_type is KeyError:
            print('This is the KeyError')

        return True


with JustSomeExceptions() as trying:
    print('Hope something good is happening here')
    c = {'adi': 2, 'edi': 3, 'marius': 4}
    print(c['george'])
    a = [2, 3, 4, 5]
    b = a[4]


@contextmanager
def just_some_exceptions():
    error_message = ''

    try:
        yield 'Just some exceptions'

    except KeyError:
        error_message = 'This is the 1st exception'
    except IndexError:
        error_message = 'This is the 2nd exception'
    finally:
        if error_message:
            print(error_message)


with just_some_exceptions() as trying:
    print('I hope something good is happening here')
    print(trying)
    a = [2, 3, 4, 5]
    b = a[4]
