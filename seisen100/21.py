# https://atcoder.jp/contests/abc023/tasks/abc023_d

# 二分探索


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
    n = inp()[0]
    hl = []
    sl = []
    for _ in range(n):
        h, s = inp()
        hl.append(h)
        sl.append(s)

    ac = 100100100100100
    wa = 0
    while wa + 1 < ac:
        wj = (wa + ac) // 2
        time_limits = []
        for i in range(n):
            time_limit = (wj - hl[i]) // sl[i]
            time_limits.append(time_limit)

        time_limits = sorted(time_limits)
        ok = True
        for i in range(n):
            if time_limits[i] < i:
                ok = False

        if ok:
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == '__main__':
    main()
