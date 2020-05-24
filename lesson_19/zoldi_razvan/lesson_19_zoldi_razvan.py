import contextlib

#  *******************************  1st approach   **********************************
# considering that we should handle KeyError I create a dictionary and because we should also
#  handle IndexError I took into consideration a LIST of dictionaries

# @contextlib.contextmanager
# def just_some_exceptions():
#     print('this is the beginning \n ')
#     error_message = ''
#     try:
#         yield data
#         x = 1 / 0  # using @contextlib.contextmanager all other exceptions will propagate outside
#         # example 'ZeroDivisionError
#     # except (KeyError, IndexError):
#     #     if KeyError and IndexError:
#     #         error_message = 'You forget to add key to one dictionary \nList do not have have desired element'
#     except KeyError:
#         error_message = 'You forget to add key to one dictionary'
#     except IndexError:
#         error_message = 'List do not have have desired element'
#     finally:
#         if error_message:
#             print(error_message)
#
#
# data = [{'name': 'Lavinia', 'age': 32},
#         {'name': 'Mihai'},  # raise exception for missing key = KeyError
#         {'name': 'Andrei', 'age': 20}]
#
# with just_some_exceptions() as missing_key:
#     print('flag 1')
#     for keys in data:
#         print('name:', keys['name'], ' -- age:', keys['age'])
#         print(data[3])  # raise exception for IndexError ; append index 3, but starting with 0 we have only 0, 1, 2
#         # print('*' * data[name])  # NameError
#     print('flag 2')


#  ******************************** 2nd approach ******************************************

# considering that we should handle KeyError I create a dictionary and because we should also
#  handle IndexError I took into consideration a LIST of dictionaries
data = [{'name': 'Lavinia', 'age': 32},
        {'name': 'Mihai'},  # raise exception for missing key = KeyError
        {'name': 'Andrei', 'age': 20}]


class JustSomeExceptions:
    def __enter__(self):
        self.original_dictionary = data
        return 'I am just a string object'

    def test_dictionary(self):
        for keys in self.original_dictionary:
            print('name:', keys['name'], ' -- age:', keys['age'])

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is KeyError:
            print('You forget to add key to one dictionary')
            return True
        elif exc_type is IndexError:
            print('List do not have have desired element')
            return True


with JustSomeExceptions() as missing_key:
    print('flag 1')
    for keys in data:
        print('name:', keys['name'], ' -- age:', keys['age'])
        # print(data[3])  # raise exception for IndexError ; append index 3, but starting with 0 we have only 0, 1, 2
        # print('*' * data[name])  # NameError is not handled bu these approaches
    print('flag 2')
