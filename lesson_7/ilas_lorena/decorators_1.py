# Create a decorator called uppercase that will uppercase the result

def uppercase(fnc):
    def uppercase_it(arg):
        return fnc(arg).upper()

    return uppercase_it


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("World"))
