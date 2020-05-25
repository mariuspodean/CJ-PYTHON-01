# Implement a context manager called just_some_exceptions that will handle
# KeyError, IndexError by printing a message and let any other exceptions
# propagate outside of the context manager.


from contextlib import contextmanager


class Just_Some_Exceptions_Class:

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is IndexError:
            print('IndexError found with class')
            return True
        elif exc_type is KeyError:
            print('KeyError found with class')
            return True
        elif exc_type:
            print('other error found with class')
            return True



@contextmanager
def just_some_exceptions_function():
    error_message = ''
    try:
        yield 'error finder here'
    except IndexError:
        error_message = 'IndexError found with function'
    except KeyError:
        error_message = 'KeyError found with function'
    except:
        error_message = 'other error found with function'
    finally:
        if error_message:
            print(error_message)


the_dict = {'nume': 4}
the_list = [0]

with just_some_exceptions_function():
    print(the_dict['Victor'])

with just_some_exceptions_function() as test:
    print(the_list[1])

with just_some_exceptions_function() as test:
    print(the_list(1))

with Just_Some_Exceptions_Class() as test:
    print(the_dict['Victor'])

with Just_Some_Exceptions_Class() as test:
    print(the_list[1])

with Just_Some_Exceptions_Class() as test:
    print(the_list(1))
