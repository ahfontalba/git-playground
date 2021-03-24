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
