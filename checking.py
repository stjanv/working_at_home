lab = """
111111111111111111
1x0010000000000001
111011101111111101
10100000000000000#
101011010101111111
101000010100001001
100011110101111101
101110010100000001
100000000101101111
101101111100100001
101001000000101001
101101111111101001
101000000000001001
101011110100101001
101000010111111001
111011110100000001
101000000101111111
101011110101010101
100000010100000001
111111111111111111""".split()
labirint2 = []
tern = []
was = {}
neighbour_x = None
neighbour_y = None
current_x = None
current_y = None

# превращение строки в список строк
def Transmut_Str_into_Mass(string):
    for i in lab:
        labirint2.append(list(i))
    for i in range(len(labirint2)):
        for j in range(len(labirint2[i])):
            if labirint2[i][j] == '1':
                labirint2[i][j] = '-1'

#coder x and #
def coder():
    labirint2[point_out[0]][point_out[1]] = 0
    labirint2[point_in[0]][point_in[1]]=1
    return labirint2

# печать списка в виде матрицы
def PrintLabirint(labirint):
    for i in labirint:
        for j in i:
            print("{:^3}".format(j), end=",")
        print("")


# поиск начальной точки
def Found_point_in(labirint):
    for i in range(len(labirint2)):
        for j in range(len(labirint2[i])):
            if labirint[j][i] == 'x':
                was[('start_cord_x', 'start_cord_y')] = (j, i)
                return (j, i)


# search exit point
def Found_point_out(labirint):
    for i in range(len(labirint2)):
        for j in range(len(labirint2[i])):
            if labirint[i][j] == '#':
                was[('exit_cord_x', 'exit_cord_y')] = (j, i)
                return (j, i)


# функция поиска выхода
def Found(labirint, pointOut):
    way = 1
    for i in range(len(labirint) * len(labirint[0])):
        way += 1
        for y in range(len(labirint)):
            for x in range(len(labirint[y])):
                if labirint[y][x] == (way - 1):
                    if y > 0 and labirint[y - 1][x] == '0':
                        labirint[y - 1][x] = way
                    if y < (len(labirint) - 1) and labirint[y + 1][x] == '0':
                        labirint[y + 1][x] = way
                    if x > 0 and labirint[y][x - 1] == '0':
                        labirint[y][x - 1] = way
                    if x < (len(labirint[y]) - 1) and labirint[y][x + 1] == '0':
                        labirint[y][x + 1] = way

                    if (abs(y - pointOut[0]) + abs(x - pointOut[1])) == 1:
                        labirint[pointOut[0]][pointOut[1]] = way
                        return True
    return False

#way print
def printWay(labirint, pointOut):
    y = pointOut[0]
    x = pointOut[1]
    way = labirint[y][x]
    result = list(range(way))
    while (way):
        way -= 1
        if y > 0 and labirint[y - 1][x] == way:
            y -= 1
            result[way] = 'down'
        elif y < (len(labirint) - 1) and labirint[y + 1][x] == way:
            result[way] = 'up'
            y += 1
        elif x > 0 and labirint[y][x - 1] == way:
            result[way] = 'right'
            x -= 1
        elif x < (len(labirint[y]) - 1) and labirint[y][x + 1] == way:
            result[way] = 'left'
            x += 1

    return result[1:]



Transmut_Str_into_Mass(lab)
point_in = Found_point_in(labirint2)
point_out = Found_point_out(labirint2)
coder()
PrintLabirint(labirint2)
if not Found(labirint2, point_out):
    print("Путь не найден!")
else:
    print('Exit is here')
print()
print(printWay(labirint2,point_out))
print()
PrintLabirint(labirint2)
print(was)
