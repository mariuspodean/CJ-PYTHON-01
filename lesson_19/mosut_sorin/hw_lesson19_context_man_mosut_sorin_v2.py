class JustSomeExceptions:

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is KeyError:
            print('Key Error !')
            return True
        if exc_type is IndexError:
            print('Index Error !')
            return True


countries_dict = {
    'Romania': 'Europe',
    'Italy': 'Europe',
    'China': 'Asia',
    'Mexic': 'Nord America'
}

numbers_list = [1, 2, 3, 4]

with JustSomeExceptions() as exceptions:
    a = countries_dict['Romania']
    print(a)
    # z = 2 / 0
    b = countries_dict['Spain']
print('*' * 10)
with JustSomeExceptions() as exceptions:
    x = numbers_list[2]
    print(x)
    # z = 2 / 0
    print(numbers_list[8])
print('*' * 10)
z = 2 / 0