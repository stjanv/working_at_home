def arithmetic(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    else:
        return "Incorrect operation"


print(arithmetic(2, 2, "0"))
