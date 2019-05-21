lab = """
111111111111111111
1x0010000000000001
111011101111111101
101010000100000001
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
1000000101000000#1
111111111111111111""".split()
print(lab)
labirint2 = []

for i in lab:
    labirint2.append(list(i))

for i in range(len(labirint2)):
    for j in range(len(labirint2[i])):
        print(labirint2[i][j], end=' ')
    print()

co_enter = [0, 0]
for i in range(len(labirint2)):
    for j in range(len(labirint2[i])):
        if labirint2[i][j] == 'x':
            co_enter = [i, j]
            y = co_enter[j]
            x = co_enter[i]
            print(co_enter)
was = {}


def Found(x0, y0):
    labirint2[x0][y0] = '2'
    if labirint2[x0][y0 + 1] == '0':
        Found(x0, y0 + 1)

    elif labirint2[x0][y0 - 1] == '0':
        Found(x0, y0 + - 1)

    elif labirint2[x0 - 1][y0] == '0':
        Found(x0 - 1, y0)

    elif labirint2[x0 + 1][y0] == '0':
        Found(x0 + 1, y0)


Found(1, 1)
for i in range(len(labirint2)):
    for j in range(len(labirint2[i])):
        print(labirint2[i][j], end=' ')
    print()
