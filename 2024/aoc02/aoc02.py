def part1():
    f = open("aoc02/file.txt", "r")
    s = 0
    for e in f:
        u = True
        t = list(map(int, e.split()))
        if t == list(sorted(t)) or t == list(sorted(t, reverse=True)):
            t = sorted(t)
            for i, j in zip(t, t[1:]):
                if j - i <= 3 and j - i > 0:
                    u = True
                else:
                    u = False
                    break
            if u is True:
                s += 1
    print(s)


def isIncreaseOrNot(o, oo):
    return o < oo


if __name__ == "__main__":
    part1()
