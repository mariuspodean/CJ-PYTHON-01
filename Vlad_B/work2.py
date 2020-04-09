# Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result

def safe_divide(fct):
    def check(first_parameter, second_parameter):
        if second_parameter == 0:
            return "Division cannot be performed"
        else:
            return fct(first_parameter, second_parameter)
    return check

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

print(divide(6, 3))
