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

was = {}
for i in range(len(lab2)):
    for j in range(len(lab2[i])):
        if lab2[x][y] == '#':
            print('we found the exit')
        else:
            if lab2[x - 1][y] != '1':
                x = x - 1
            elif lab2[x + 1][y] != '1':
                x = x + 1
            elif lab2[x][y - 1] != '1':
                y = y - 1
            elif lab2[x][y + 1] != '1':
                y = y + 1
        print(lab2[x][y])
print()