a = [[0] * 15 for _ in range(15)]
a[0][7] = 1
a[1][6] = a[1][8] = 1
a[2][5] = a[2][9] = 1
a[3][4] = a[3][10] = 1
a[4][3] = a[4][11] = 1
a[5][2] = a[5][12] = 1
a[6][1] = a[6][13] = 1
a[7][0] = a[7][14] = 1
a[8][1] = a[8][13] = 1
a[9][2] = a[9][12] = 1
a[10][3] = a[10][11] = 1
a[11][4] = a[11][10] = 1
a[12][5] = a[12][9] = 1
a[13][6] = a[13][8] = 1
a[14][7] = 1


s = 0


def f(x, y):
    global s
    if a[x][y] != 1:
        a[x][y] = 1
        if a[x + 1][y] == a[x][y + 1] == a[x - 1][y] == a[x][y - 1] == 1:
            s += 1
        f(x + 1, y)
        f(x, y - 1)
        f(x - 1, y)
        f(x, y + 1)


f(7, 7)
print(s - 1)
