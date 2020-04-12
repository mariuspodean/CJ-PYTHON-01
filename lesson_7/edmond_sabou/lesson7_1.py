import random


def uppsercase(func):

    annotations = ["-", "*", "+", "-", "="]
    annotate = random.choice(annotations)

    def formatting(*args):
        print(annotate * 20)
        print(func(*args).upper())
        print(annotate * 20)

    return formatting


@uppsercase
def print_message(name):
    return "  Greetings {}!".format(name)


print_message("World")

