def safe_divide(func):

    def verify(*args):

        try:
            result = func(*args)

        except ZeroDivisionError as zero_err:
            raise Exception(f"Sorry! {zero_err} error occurred. Consider NOT dividing by zero!")

        except TypeError as type_err:
            raise Exception(f"Oops! {type_err} error occurred.")

        else:
            return result

    return verify


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


a = divide(10, 2)
print(a * 5)

