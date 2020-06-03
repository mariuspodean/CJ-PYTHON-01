from itertools import chain

items = [1, 2, 3, 4, 5]

def multiply(x):
    return x*x

def add(x):
    return x+x

print(list(map(lambda x: add(multiply(x)), items)))
print(list(map(lambda x: multiply(add(x)), items)))
the_list = list(chain(*map(lambda x: (add(x), multiply(x)), items)))

print(the_list)

# print(list(map(lambda x: add(x), items), map(lambda x: multiply(x), items)))
# 2 1 4 4 6 9