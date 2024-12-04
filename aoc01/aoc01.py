def part1():
    f = open("file", "r")
    left, right = [], []
    for e in f:
        t = e.split()
        left.append(int(t[0]))
        right.append(int(t[1]))

    left = sorted(left)
    right = sorted(right)

    s = []
    for e, j in zip(left, right):
        s.append(max(e, j) - min(e, j))
    print(sum(s))


def part2():
    f = open("file", "r")
    left, right = [], []
    for e in f:
        t = e.split()
        left.append(int(t[0]))
        right.append(int(t[1]))

    s = []
    for e in left:
        t = right.count(e)
        s.append(e * t)

    print(sum(s))


if __name__ == "__main__":
    part1()
    part2()
