# def path():


def partone(matrice):
    x = 0
    y = 0
    dir = 0
    for k, e in enumerate(matrice):
        for j, i in enumerate(e):
            if i == '^':
                y, x = k, j
                break

    while y > 0 and y < len(matrice) - 1  and x > 0 and y < len(matrice[y]) - 1:
        if dir == 0:
            while y >= 0 and matrice[y][x] != '#':
                matrice[y][x] = 'X'
                y -= 1
                if y >= 0 and matrice[y][x] == '#':
                    dir = (dir + 1) if dir < 3 else 0
                    y += 1
                    matrice[y][x] = '>'
                    break
                if y > 0:
                    matrice[y][x] = '^'
        if dir == 1:
            while x < len(matrice[y]) and matrice[y][x] != '#':
                matrice[y][x] = 'X'
                x += 1
                if x < len(matrice[y]) and matrice[y][x] == '#':
                    dir = (dir + 1) if dir < 3 else 0
                    x -= 1
                    matrice[y][x] = 'V'
                    break
                if x < len(matrice[y]):
                    matrice[y][x] = '>'
        elif dir == 2:
            while y < len(matrice) and matrice[y][x] != '#':
                matrice[y][x] = 'X'
                y += 1
                if y < len(matrice) and  matrice[y][x] == '#':
                    dir = (dir + 1) if dir < 3 else 0
                    y -= 1
                    matrice[y][x] = '<'
                    break
                if y < len(matrice):
                    matrice[y][x] = 'V'

        elif dir == 3:
            while x >= 0 and matrice[y][x] != '#':
                matrice[y][x] = 'X'
                x -= 1
                if x >= 0 and matrice[y][x] == '#':
                    dir = (dir + 1) if dir < 3 else 0
                    x += 1
                    matrice[y][x] = '^'
                    break
                if x > 0:
                    matrice[y][x] = '<'

    ff = open("test.txt", "w")
    s = ""
    for e in matrice:
        s += "".join(str(i) for i in e)
        s += '\n'
    ff.write(s)
    ff.close()
    c = 0
    for e in matrice:
        c += e.count('X')
    print(c)


# def parttwo(matrice):




if __name__ == "__main__":
    f = open("file.txt", "r").readlines()
    matrice = [[i for i in e[:-1]] for e in f]
    partone(matrice)
    # parttwo(matrice)
