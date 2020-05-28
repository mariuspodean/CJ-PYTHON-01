"""
Implement a context manager called just_some_exceptions that will handle KeyError, IndexError by printing a message and let any other exceptions propagate outside of the context manager.
Implement the context manager by using both approaches: by using class and by using @contextmanager
Write examples that prove the functionality for all the handled exceptions and for one exception that is not handled.
"""
import contextlib


class Just_some_execeptions1():

    def __init__(self, dct):
        self.dct = dct
        print(f'input arg: {self.dct}')

    def __enter__(self):
        print("updating the dict:")
        self.dct.update({'key3':'value3'})
        return self.dct

    def __exit__(self, exc_type, exc_value, traceback):
        del self.dct['key3']
        if exc_type is KeyError:
            print('This is a KeyError message')
            return True
        if exc_type is IndexError:
            print('This is an IndexError message')
            return True


@contextlib.contextmanager
def Just_some_execeptions2(dct):
    dct.update({'key4':'value4'})

    error_message = ''
    try:
        yield dct
    except KeyError:
        error_message = 'This is a KeyError message'
    except IndexError:
        error_message = 'This is a IndexError message'
    finally:
        if error_message:
            print(error_message)

dc = {'key1':'value1', 'key2':'value2'}
with Just_some_execeptions1(dc) as thing:
    print(f'CM1: show updated dict: {thing}')
    thing['key5']

with Just_some_execeptions2(dc) as thing:
    print(f'CM2: show updated dict: {thing}')
    lst = list(thing)
    lst[7] = 10

with Just_some_execeptions2(dc) as thing:
    print(f'CM3: show updated dict: {thing}')
    print(1/0)
