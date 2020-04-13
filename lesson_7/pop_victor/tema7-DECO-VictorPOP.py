# first part :
def uppercase(fnc):
    print('uppercasing for {}'.format(fnc))

    def inner_func(var):
        print('the variable : {}'.format(var))
        return fnc(var).upper()
    return inner_func


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet('World of WarCraft'))
print(greet('second chance'))

# second part :
print()


def safe_divide(fnc):
    print('save divide for {}'.format(fnc))

    def wrapper(var1, var2):
        print('dividing {} by {}'.format(var1, var2))
        if type(var1) != int:
            print("{} can't be divided since it's a {}".format(var1, type(var1)))
            return None
        if var2 == 0 or type(var2) != int:
            print("can't divide by {}".format(var2))
            return None
        return fnc(var1, var2)
    return wrapper


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


print(divide(10, 5))
print(divide(10, 0))
print(divide(10, 'x'))
print(divide('y', 0))
print(divide('xyz', 'y'))

# third part :
print()

print_registry = []


def register(fnc):
    print('registering {}'.format(fnc))
    print_registry.append(fnc.__name__)
    return fnc


@register
def greetings(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(print_registry)
print(greetings("young man"))
print(say_hello('Noob'))
print(say_goodbye('Friend'))
