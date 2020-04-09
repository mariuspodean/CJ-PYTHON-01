def uppercase(func):
    def uppercasing(arg):
        return func(arg).upper()

    return uppercasing


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("World"))
# >>> "GREETINGS WORLD!"
