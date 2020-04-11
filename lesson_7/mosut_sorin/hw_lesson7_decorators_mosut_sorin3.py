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
    def iner_register(args):
        fnc_name = str(fnc)
        fnc_name = fnc_name.split(' ')
        print_registry.append(fnc_name[1])

    return iner_register


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


greet('Sorin')
say_hello('Sorin')
say_goodbye('Sorin')

print(print_registry)

