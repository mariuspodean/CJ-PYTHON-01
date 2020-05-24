'''
Given the following function:
def divide(first_number, second_number):
 return first_number / second_number
Create a decorator called safe_divide that will output a message
if the division cannot be performed, othervise it will return the result.
'''

def safe_divide(fnc):

    def verif_fnc(*args):
        if args[1] == 0:
            return 'divide by 0'
        else:
            return args[0] / args[1]

    return verif_fnc

@safe_divide
def divide(first_number, second_number):
    return first_number / second_number

x = divide(5,3)
print(f'{x:.2f}')
print(f'{x * 5:.2f}')
