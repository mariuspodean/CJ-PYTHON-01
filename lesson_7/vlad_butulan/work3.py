# Create a decorator called register that will update a list called print_registry with all the decorated functions names
print_registry = []

def register(fct):
    print_registry.append(fct.__code__.co_name)
    def inner(*args):
        return fct(*args)
    return inner

@register
def greet(name):
    return "Greetings {}!".format(name)

def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)

print(greet("gigi"))
print(say_hello("cucu"))
print(say_goodbye("bubu"))

print(print_registry)