import itertools

items = [1, 2, 3, 4, 5, 6]


def multiply(x):
    return x * x


def add(x):
    return x + x


# apply map, obtain list of lists
multiple_func = list(map(lambda i: [add(i), multiply(i)], items))

# unpack and merge into single list
merged = list(itertools.chain.from_iterable(multiple_func))

print(merged)
