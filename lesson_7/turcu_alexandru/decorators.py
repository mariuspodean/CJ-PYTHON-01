def uppercase(greetings):
    def upper(*args):
        return greetings(*args).upper()
    return upper


print('-' * 20)


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("World"))
print('-' * 20)


def safe_divide(func):
    def inner_func(first_number, second_number):
        if second_number == 0:
            return print('Division cannot be performed')
        return func(first_number, second_number)
    return inner_func


@safe_divide
def divide(first_number, second_number):
    return print(first_number / second_number)


divide(1, 0)
divide(420, 69)
print('-' * 20)


print_registry = []


def register(func):
    def update_registry(func_name):
        print_registry.append(func_name.__name__)
    return update_registry(func)


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(print_registry)
print('-' * 20)