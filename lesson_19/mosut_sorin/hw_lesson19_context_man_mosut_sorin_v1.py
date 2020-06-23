import contextlib


@contextlib.contextmanager
def just_some_exceptions():

    error_message = ''
    try:
        yield
    except KeyError:
        error_message = 'KeyError !'
    except IndexError:
        error_message = 'IndexError !'
    finally:
        if error_message:
            print(error_message)


countries_dict = {
    'Romania': 'Europe',
    'Italy': 'Europe',
    'China': 'Asia',
    'Mexic': 'Nord America'
}

numbers_list = [1, 2, 3, 4]

with just_some_exceptions() as exception:
    a = countries_dict['Romania']
    print(a)
    b = countries_dict['Spain']
    # X = 2 / 0
print('*' * 10)
with just_some_exceptions() as exception:
    print(numbers_list[2])
    print(numbers_list[8])
    # X = 2 / 0
print('*' * 10)
z = 2 / 0