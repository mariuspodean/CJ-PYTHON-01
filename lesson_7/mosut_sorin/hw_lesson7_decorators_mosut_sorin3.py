'''

    Given a set of print methods:

print_registry = []


def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


def say_goodbye(name):
    return "Goodbye {}!".format(name)

Create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []

@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)
['greet', 'say_goodbye']

'''

print_registry = []


def register(fnc):
    fnc_name = str(fnc).split(' ')
    print_registry.append(fnc_name[1])
    return fnc


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(greet('Sorin'))
print(say_hello('Sorin'))
print(say_goodbye('Sorin'))

print('\n',print_registry)
