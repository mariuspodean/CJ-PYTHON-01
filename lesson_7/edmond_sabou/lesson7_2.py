def safe_divide(func):

    def verify(*args):

        try:
            result = func(*args)
        except ZeroDivisionError as zero_err:
            print(f"Sorry! {zero_err} occurred. Try NOT dividing by zero!")
            pass
        except TypeError as type_err:
            print(f"Oops! {type_err} error occurred.")
            pass
        else:
            return result

    return verify


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


a = divide(10, 2)
print(a * 5)

