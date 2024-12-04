def partone():
    f = open("file.txt", "r").readlines()
    rules = {}
    for e in f:
        tmp = [int(i) for i in e.strip().split("|")]
        if tmp[0] in rules:
            rules[tmp[0]].append(tmp[1])
        else:
            rules[tmp[0]] = [tmp[1]]

    f = open("file01.txt", "r").readlines()
    s = 0
    for e in f:
        correct = True
        tmp = [int(i) for i in e.replace("\n", "").split(",")]
        for i in range(len(tmp)):
            if tmp[i] in rules.keys():
                for j in rules[tmp[i]]:
                    if j in tmp[:i]:
                        correct = False
                        break

        if correct is True:
            s += tmp[int(len(tmp) / 2)]
        print(s)


def parttwo():
    print("______________________________________________")
    f = open("file.txt", "r").readlines()
    rules = {}
    for e in f:
        tmp = [int(i) for i in e.strip().split("|")]
        if tmp[0] in rules:
            rules[tmp[0]].append(tmp[1])
            rules[tmp[0]] = sorted(rules[tmp[0]], reverse=True)

        else:
            rules[tmp[0]] = [tmp[1]]

    f = open("file01.txt", "r").readlines()
    s = 0
    for e in f:
        correct = True
        tmp = [int(i) for i in e.replace("\n", "").split(",")]
        i = 0
        while i != len(tmp):
            if tmp[i] in rules.keys():
                for j in rules[tmp[i]]:
                    if j in tmp[:i]:
                        correct = False
                        print(tmp)
                        tmp[tmp.index(j)] = tmp[i]
                        tmp[i] = j
                        i = 0
                        print(
                            tmp,
                            "haha",
                        )
            i += 1

        if correct is False:
            s += tmp[int(len(tmp) / 2)]
        print(s)


if __name__ == "__main__":
    # partone()
    parttwo()
