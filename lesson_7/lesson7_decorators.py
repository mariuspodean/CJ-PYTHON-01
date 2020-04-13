# "GREETINGS WORLD!"

def uppercase(fnc):
    def inner_fnc(*args):
        initial_str = fnc(*args)
        uppercase_str = initial_str.upper()
        return uppercase_str

    return inner_fnc


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet('world'))


# Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.

def safe_divide(fnc):

   def wrapper(*args, **kwargs):
        try:
            return fnc(*args, **kwargs)
        except Exception as e:
            print("Division by zero error")
   return wrapper


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


print(divide(5, 0))


# Create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []


def register(fnc):
    print_registry.append(fnc.__name__)
    return fnc


@register
def greet(name):
    return "Greeting {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(print_registry)

