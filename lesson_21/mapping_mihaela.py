import itertools
items = [1, 2, 3, 4, 5]


def multiply(x):
    return x * x


def add(x):
    return x + x


my_list = list(map(lambda x: (add(x), multiply(x)), items))
my_new_list= list(itertools.chain.from_iterable(my_list))
print(my_new_list)
