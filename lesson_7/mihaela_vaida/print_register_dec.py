print_registry = []


def register(fnc):
    return print(print_registry.append(fnc.__name__))


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(say_hello('Vio'))  # 'Hello Vio!'

print(print_registry)  # ['greet', 'say_goodbye']
