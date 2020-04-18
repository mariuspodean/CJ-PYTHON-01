# Create a decorator called uppercase that will uppercase the result
def uppercase(fct):
    def upper(naming):
        return naming.upper()
    return upper


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("gigi"))
