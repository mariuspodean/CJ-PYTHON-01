from itertools import count
from numpy import repeat


def multiply(x):
    return x * x


def add(x):
    return x + x


items = [1, 2, 3, 4, 5]

results = list(map(lambda x: add(x[1]) if x[0] % 2 else multiply(x[1]), zip(count(1), repeat(items, 2))))

print(results)
