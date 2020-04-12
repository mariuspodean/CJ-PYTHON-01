
# 1. Given the following function:

    #d ef greet(name):
     # return "Greetings {}!".format(name)

# Create a decorator called uppercase that will uppercase the result

# @uppercase
# def greet(name):
    # return "Greetings {}!".format(name)

# print(greet("World"))
# >>> "GREETINGS WORLD!"


def uppercase(func):
    def inside(name):
        original=func(name)
        modified=str.upper(original)
        return modified
    return inside

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))


# 2. Given the following function:

    # def divide(first_number, second_number):
     # return first_number / second_number

# Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.

def safe_divide(func):
    def inside(numerator, denominator):
        if denominator==0:
            print("Can't divide by 0")
            return
        func(numerator, denominator)
    return inside

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

print(divide(10, 0))



# 3. Given a set of print methods:

print_registry = []


def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


def say_goodbye(name):
    return "Goodbye {}!".format(name)

# Create a decorator called register that will update a list called print_registry with all the decorated functions names.

# print_registry = []

# @register
# def greet(name):
    # return "Greetings {}!".format(name)


# def say_hello(name):
    # return "Hello {}!".format(name)

# @register
# def say_goodbye(name):
    # return "Goodbye {}!".format(name)

# print(print_registry)
# >>> ['greet', 'say_goodbye']


print_registry = []

def register(func):
    global print_registry
    print_registry.append(func.__name__)
    def inside(name):
        func(name)
    return inside

@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(print_registry)
