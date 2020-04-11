print_registry = []


def register(fnc):
    def print_register(arg):
        print_registry.append(fnc.__name__)
        print(print_registry)

    return print_register


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


greet('dsdas')  # ['greet']
print(say_hello('Vio'))  # 'Hello Vio!'
say_goodbye('sads')  # ['greet', 'say_goodbye']
say_goodbye('sads')
greet('dsdas')