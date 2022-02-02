"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube, power, mod, )

while True:

    # Asks user for input.

    input_string = input('Enter your equation. ')

    # Splits list into items.

    input_string_list = input_string.split(' ')

    # Sorts inputs by type.

    if 'q' in input_string_list:
        break
    elif len(input_string_list) == 3:
        operator = input_string_list[0]
        var1 = int(input_string_list[1])
        var2 = int(input_string_list[2])
    elif len(input_string_list) == 2:
        operator = int(input_string_list[0])
        var1 = int(input_string_list[1])
    else:
        print('That is not a valid entry.')

    # Checks if input is integer

    if type(var1) is not int or type(var2) is not int:
        print('That is not a number.')
    else:
        if operator == 'add':
            result = add(var1, var2)
            print(result)
        elif operator == 'subtract':
            result = subtract(var1, var2)
            print(result)
        elif operator == 'multiply':
            result = multiply(var1, var2)
            print(result)
        elif operator == 'divide':
            result = divide(var1, var2)
            print(result)
        elif operator == 'pow':
            result = power(var1, var2)
            print(result)
        elif operator == 'mod':
            result = mod(var1, var2)
            print(result)
        elif operator = 'square':
            result = square(var1)
            print(result)
        elif operator = 'cube':
            result = cube(var1)
            print(result)