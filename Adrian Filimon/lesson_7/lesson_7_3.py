# Given a set of print methods:
# print_registry = []
#
#
# def greet(name):
#     return "Greetings {}!".format(name)
#
#
# def say_hello(name):
#     return "Hello {}!".format(name)
#
#
# def say_goodbye(name):
#     return "Goodbye {}!".format(name)
# Create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []


def register(funct):
    def inner_funct(*args):
        return print_registry.append(funct.__name__)

    return inner_funct


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

say_hello('Cristi')
greet('Cordelia')
say_goodbye('Hollywood')

print(print_registry)
