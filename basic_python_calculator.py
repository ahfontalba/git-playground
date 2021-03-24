def validate_operator(operator):
    if operator in ('x', '+', '-', '/'):
        return True
    return False

def calculate(operation, operand_a, operand_b):
    if '*' == operation:
        return operand_a * operand_b
    elif '+' == operation:
        return operand_a + operand_b
    elif '-' == operation:
        return operand_a - operand_b
    elif '/' == operation:
        return operand_a / operand_b
    
    return 0



operator = input("Enter operation to perform: 'x', '+', '-' or '/' : ")

if validate_operator(operator):

    try:
        operand_a = int(input("Enter an integer : "))
        operand_b = int(input("Enter another integer : "))

        result = calculate(operator, operand_a, operand_b)

        print(int(result))

    except ValueError:
        print('Invalid integer')

else:
    print('Invalid operator')

