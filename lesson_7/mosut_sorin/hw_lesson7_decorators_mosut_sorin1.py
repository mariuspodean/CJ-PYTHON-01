'''
Given the following function:

def greet(name):
    return "Greetings {}!".format(name)

Create a decorator called uppercase that will uppercase the result

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))
"GREETINGS WORLD!"


def greet(name):
    return "Greetings {}!".format(name)

'''

def uppercase(greet):

    def uppercase_in(*args):

        z = str.upper(greet(*args))

        return z

    return uppercase_in

@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))


