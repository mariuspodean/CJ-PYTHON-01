# Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it
# will return the result.


def safe_divide(fnc):
    def check_result(arg1, arg2):

        try:
            return arg1 / arg2

        except ZeroDivisionError:
            return 'Division cannot be performed!'

    return check_result


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


print(divide(12, 3))
print(divide(12, 0))
