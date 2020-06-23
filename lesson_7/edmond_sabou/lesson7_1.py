def uppsercase(func):

    def formatting(*args):

        return func(*args).upper()

    return formatting


@uppsercase
def print_message(name):
    return "Greetings {}!".format(name)


msg = print_message("World!")
print(msg)
