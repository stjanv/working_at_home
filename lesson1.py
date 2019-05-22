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
if labirint2[x0][y0] == '#':
    print('exit found')
else:
    if labirint2[x0][y0] == 'x':
        labirint2[x0][y0] = 'x'
        was[('enter_point_cord_x', 'enter_point_cord_y')] = (x0, y0)
    else:
        labirint2[x0][y0] = 2
    if labirint2[x0][y0 + 1] == '0' or labirint2[x0][y0 + 1] == '#':
        tern.append('r')
        Found(x0, y0 + 1)
    if labirint2[x0][y0 - 1] == '0' or labirint2[x0][y0 - 1] == '#':
        tern.append('l')
        Found(x0, y0 - 1)
    if labirint2[x0 - 1][y0] == '0' or labirint2[x0 - 1][y0] == '#':
        tern.append('u')
        Found(x0 - 1, y0)
    if labirint2[x0 + 1][y0] == '0' or labirint2[x0 + 1][y0] == '#':
        tern.append('d')
        Found(x0 + 1, y0)


        def coder_lab(labirint, pointIn, pointOut):
            pointIn_x = pointIn[0]
            pointIn_y = pointIn[1]
            pointOut_x = pointOut[0]
            pointOut_y = pointOut[1]
            labirint[pointIn_x][pointIn_y] == '='
            labirint[pointOut_x][pointOut_y] == 0
            return labirint