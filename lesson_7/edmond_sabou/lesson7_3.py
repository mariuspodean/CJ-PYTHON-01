print_registry = []


def register(func):

    def appender(*args):

        return print_registry.append(func.__name__)

    return appender


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


greet("Edi")
say_hello("Hello!")
say_goodbye("BBye!")
print(print_registry)

