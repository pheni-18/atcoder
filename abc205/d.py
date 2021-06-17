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
    n, q = inp()
    al = inp()
    cl = [0]
    ma = {}
    for i in range(n):
        if i == 0:
            diff = al[i] - 1
        else:
            diff = al[i] - al[i - 1] - 1
        c = cl[i] + diff
        ma[c] = al[i]
        cl.append(c)

    ansl = []
    for i in range(q):
        k = inp()[0]
        wa = 0
        ac = len(cl)
        while wa + 1 < ac:
            wj = wa + (ac - wa) // 2
            if cl[wj] >= k:
                ac = wj
            else:
                wa = wj

        cur = ac - 1
        if cur == 0:
            ansl.append(k)
        else:
            c = cl[cur]
            ans = ma[c] + k - c
            ansl.append(ans)

    for ans in ansl:
        print(ans)


if __name__ == '__main__':
    main()
