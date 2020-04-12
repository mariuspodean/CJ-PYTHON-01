# Create a decorator called register that will update a list called print_registry with all the decorated functions
# names.


def register(fnc):
    
    def updater(args):
        print_registry.append(fnc.__name__)    
    
    return updater


print_registry = []


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


greet('Lorena')
say_hello('Lorena')
say_goodbye('Lorena')

print(print_registry)
