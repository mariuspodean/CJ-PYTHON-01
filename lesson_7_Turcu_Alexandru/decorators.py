def uppercase(greetings):
    def upper(*args):
        return greetings(*args).upper()
    return upper
print('-' * 20)
@uppercase
def greet(name):
    return "Greetings {}!".format(name)

print(greet("World"))

print('-' * 20)
