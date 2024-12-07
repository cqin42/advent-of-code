import numpy as np


def partone():
    f = open("file.txt", "r").readlines()
    s = 0
    l = [[i for i in e] for e in f]

    fVertical = ""
    for e in range(len(f)):
        for i in range(len(f)):
            fVertical += f[i][e]
        fVertical += "\n"

    for e, j in zip(f, fVertical.split("\n")):
        s += e.count("XMAS") + e.count("SAMX")
        s += j.count("XMAS") + j.count("SAMX")

    diag = []
    for e in range(len(l[0])):
        tmp = "".join(i for i in np.diag(l, e))
        diag.append(tmp)
        s += tmp.count("XMAS") + tmp.count("SAMX")

    diagReverse = []
    lReverse = [[i for i in e[::-1]] for e in f]
    for e in range(len(lReverse[0])):
        tmp = "".join(i for i in np.diag(lReverse, e))
        diagReverse.append(tmp)
        s += tmp.count("XMAS") + tmp.count("SAMX")

    for e in range(len(l[0])):
        tmp = "".join(i for i in np.diag(l[::-1], e))
        if tmp[::-1] not in diag and tmp[::-1] not in diagReverse:
            s += tmp.count("XMAS") + tmp.count("SAMX")

    lReverse = [[i for i in e[::-1]] for e in f]
    for e in range(len(lReverse[0])):
        tmp = "".join(i for i in np.diag(lReverse[::-1], e))
        if tmp[::-1] not in diag and tmp[::-1] not in diagReverse:
            s += tmp.count("XMAS") + tmp.count("SAMX")

    print(s)


def parttwo():
    f = open("file.txt", "r").readlines()
    s = 0
    l = [[i for i in e] for e in f]
    # print(l)
    for i in range(1, len(l) - 1):
        for j in range(1, len(l[0]) - 1):
            if l[i][j] == "A":
                if (
                    l[i - 1][j - 1] == "M"
                    and l[i + 1][j - 1] == "M"
                    and l[i - 1][j + 1] == "S"
                    and l[i + 1][j + 1] == "S"
                ):
                    s += 1
                elif (
                    l[i - 1][j - 1] == "S"
                    and l[i + 1][j - 1] == "S"
                    and l[i - 1][j + 1] == "M"
                    and l[i + 1][j + 1] == "M"
                ):
                    s += 1
                # elif (
                #     l[i - 1][j - 1] == "S"
                #     and l[i + 1][j - 1] == "M"
                #     and l[i - 1][j + 1] == "M"
                #     and l[i + 1][j + 1] == "S"
                # ):
                #     s += 1
                elif (
                    l[i - 1][j - 1] == "S"
                    and l[i + 1][j - 1] == "M"
                    and l[i - 1][j + 1] == "S"
                    and l[i + 1][j + 1] == "M"
                ):
                    s += 1
                # elif (
                #     l[i - 1][j - 1] == "M"
                #     and l[i + 1][j - 1] == "S"
                #     and l[i - 1][j + 1] == "S"
                #     and l[i + 1][j + 1] == "M"
                # ):
                #     s += 1
                elif (
                    l[i - 1][j - 1] == "M"
                    and l[i + 1][j - 1] == "S"
                    and l[i - 1][j + 1] == "M"
                    and l[i + 1][j + 1] == "S"
                ):
                    s += 1
        # MMSS, SSMM, SMSM, MSSM, SMMS, MSMS
    print(s)


if __name__ == "__main__":
    partone()
    parttwo()
