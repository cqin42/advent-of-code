def partone(f, ff):
    rules = {}
    for e in f:
        key, value = map(int, e.strip().split("|"))
        rules.setdefault(key, []).append(value)

    s = 0
    for e in ff:
        tmp = list(map(int, e.strip().split(",")))
        for i, value in enumerate(tmp):
            if value in rules and any(j in tmp[:i] for j in rules[value]):
                break
        else:
            s += tmp[len(tmp) // 2]
    print(s)


def parttwo(f, ff):
    rules = {}
    for e in f:
        key, value = map(int, e.strip().split("|"))
        rules.setdefault(key, []).append(value)

    s = 0
    for e in ff:
        correct = True
        tmp = list(map(int, e.strip().split(",")))
        i = 0
        while i < len(tmp):
            for j in rules[tmp[i]]:
                if j in tmp[:i]:
                    correct = False
                    tmp[tmp.index(j)], tmp[i] = tmp[i], j
                    i = 0
            i += 1
        s += tmp[len(tmp) // 2] if not correct else 0
    print(s)


if __name__ == "__main__":
    f = open("file.txt", "r").readlines()
    ff = open("file01.txt", "r").readlines()
    partone(f, ff)
    parttwo(f, ff)
