# Create a decorator called uppercase that will uppercase the result of function greet


def uppercase(fnc):
    def fnc2(none_arg):
        return fnc(none_arg).upper()
    return fnc2


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("World"))

# Given the following function:
# Create a decorator called safe_divide that will output a message if the division cannot be performed, otherwise it
# will return the result.

import sys


def safe_divide(fnc):
    def div(num1, num2):
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("You can't divide by zero!")
            sys.exit()

    return div


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


user_input1 = int(input("Please enter first number: "))
user_input2 = int(input("Please enter second number: "))
print(divide(user_input1, user_input2))


# Given a set of print methods, Create a decorator called register that will update a list called print_registry with
# all the decorated functions names.
import inspect

print_registry = []


# original code at: https://stackoverflow.com/questions/52191968/check-if-a-function-was-called-as-a-decorator
# documentation at https://docs.python.org/3/library/inspect.html
def register1(fnc):
    lines = inspect.stack(context=2)[1].code_context
    decorated = any(line.startswith('@') for line in lines)
    if decorated:
        print_registry.append(fnc.__name__)
    return fnc


@register1
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register1
def say_goodbye(name):
    return "Goodbye {}!".format(name)


# print(say_hello.__name__)  #test how __name__ works
print(list(print_registry))
