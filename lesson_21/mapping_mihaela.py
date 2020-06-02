items = [1, 2, 3, 4, 5]


def multiply(x):
    return x * x


def add(x):
    return x + x


my_list = list(map(lambda x: (add(x), multiply(x)), items))

print(my_list)
