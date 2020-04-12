# Given the following function:
# def divide(first_number, second_number):
#  return first_number / second_number
# Create a decorator called safe_divide that will output a message if the division cannot be performed,
# othervise it will return the result.


def safe_divide(funct):

    def inner_function(*args):
        try:
            test = funct(*args)
        except ZeroDivisionError as zde:
            print(f'Not a good idea, there is a {zde} error, Luke :)')
        except TypeError as te:
            print(f'Not even now have you got it right, there is a {te} error going on, my son :-)')
        else:
            return print(test)
        finally:
            print("Young padawan!!")


    return inner_function

# try -> except > else > finally
@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


divide(4, 'a')
