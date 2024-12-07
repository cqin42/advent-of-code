import itertools


def partone(f):
    d = {}
    for e in f:
        key, values = e.split(":")
        values = list(map(int, values.replace("\n", "").split()))
        d[int(key)] = values

    result = 0
    for e in d:
        tmp = list(itertools.product(["+", "*", "||"], repeat=len(d[e]) - 1))
        for j in tmp:
            sum = d[e][0]
            for i, value in enumerate(d[e][1:]):
                if j[i - 1] == "+":
                    sum += value
                elif j[i - 1] == "*":
                    sum *= value
                else:
                    sum = int(str(sum) + str(value))
            if sum == e:
                result += e
                break
    print(result)


if __name__ == "__main__":
    f = open("file.txt", "r").readlines()
    partone(f)
