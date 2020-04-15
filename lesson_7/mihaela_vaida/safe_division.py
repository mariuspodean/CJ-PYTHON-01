def safe_divide(fnc):
    def exception(arg1, arg2):
        try:
            if type(arg1 / arg2) == int or type(arg1 / arg2) == float or arg2 != 0:
                print(arg1 / arg2)


        except:
            print("The division cannot be performed")

    return exception


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


divide(15, 0)  # The division cannot be performed
divide('dsads', 'dssa')  # The division cannot be performed
divide('abc', 34.3)  # The division cannot be performed
divide(12, '3232')  # The division cannot be performed
divide(12.3, 3)  # 4.1000000000000005
