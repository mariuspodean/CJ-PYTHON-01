
print_registry = []
def register(fnc):
    
    
    def print_register(*args):        
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
