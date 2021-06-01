def inp(to_int=False):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    l = sl2il(l) if to_int else l
    return l[0] if len(l) == 1 else l


def inps(n, to_int=False):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def sl2il(l):
    return list(map(lambda x: int(x), l))


def il2sl(l):
    return list(map(lambda x: str(x), l))


def main():
    n = inp(True)
    ps = inps(n, True)

    ac = 0
    wa = 1001001001
    m = 5
    while ac + 1 < wa:
        wj = (ac + wa) // 2
        s = set()
        for i in range(n):
            t = 0
            for j in range(m):
                if ps[i][j] >= wj:
                    t += 1 << j
            s.add(t)

        ok = False
        for x in s:
            for y in s:
                for z in s:
                    if x | y | z == (1 << m) - 1:
                        ok = True

        if ok:
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == '__main__':
    main()
