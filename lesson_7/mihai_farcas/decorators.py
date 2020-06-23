#     def greet(name):
#      return "Greetings {}!".format(name)
#
#     Create a decorator called uppercase that will uppercase the result
#
# @uppercase
# def greet(name):
#     return "Greetings {}!".format(name)
#
# print(greet("World"))
# >>> "GREETINGS WORLD!"
def uppercase(fnc):
    def upp(arg):
        return fnc(arg).upper()
    return upp


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("World"))
print(greet('asl'))


# Given the following function:
#
# def divide(first_number, second_number):
#  return first_number / second_number
#
# Create a decorator called safe_divide that will output a message if
# the division cannot be performed, othervise it will return the result.

def safe_divide(fct):
    def it_can_be_divided(first_number, second_number):
        if first_number != 0 or second_number != 0:
            fct(first_number, second_number)
        else:
            print('The division cannot be performed')
    return it_can_be_divided

@safe_divide
def divide(f1, f2):
    return round(float(f1 / f2), 2)


print(divide(2, 3))
print(divide(0, 3))
# print(divide(3, 0))

#     Given a set of print methods:
#
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
#
# Create a decorator called register that will update a list called print_registry
# with all the decorated functions names.
#
# print_registry = []
#
# @register
# def greet(name):
#     return "Greetings {}!".format(name)
#
#
# def say_hello(name):
#     return "Hello {}!".format(name)
#
# @register
# def say_goodbye(name):
#     return "Goodbye {}!".format(name)
#
# print(print_registry)
# >>> ['greet', 'say_goodbye']

print_registry = []


def register(fct):
    print_registry.append(fct.__name__)
    return fct


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(print_registry)

print(greet('world'))
print(say_goodbye('world'))
