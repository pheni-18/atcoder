def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    n, k = inp()
    all = []
    for _ in range(n):
        al = inp()
        all.append(al)

    mi = ((k ** 2) // 2) + 1
    wa = -1
    ac = 1001001001
    while wa + 1 < ac:
        wj = (wa + ac) // 2
        cll = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                cll[i + 1][j + 1] = 1 if all[i][j] > wj else 0

        for i in range(n + 1):
            for j in range(n):
                cll[i][j + 1] += cll[i][j]

        for i in range(n):
            for j in range(n + 1):
                cll[i + 1][j] += cll[i][j]

        ok = False
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                cum = cll[i+k][j+k] - cll[i][j+k] - cll[i+k][j] + cll[i][j]
                if cum < mi:
                    ok = True

        if ok:
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == '__main__':
    main()
