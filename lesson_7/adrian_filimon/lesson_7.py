# Given the following function:
# def greet(name):
#  return "Greetings {}!".format(name)
# Create a decorator called uppercase that will uppercase the result
# @uppercase
# def greet(name):
#     return "Greetings {}!".format(name)
#
# print(greet("World"))
# >>> "GREETINGS WORLD!"


def uppercase(func):

    def inner_function(*args):

        return func(*args).upper()

    return inner_function

@uppercase
def greet(name):
    return f"Greetings {name}!"


print(greet("Viola"))
