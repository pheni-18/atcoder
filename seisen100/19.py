# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b

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
    d = inp()[0]
    n = inp()[0]
    m = inp()[0]
    sl = [0]
    for _ in range(n - 1):
        sl.append(inp()[0])
    sl.append(d)
    kl = [inp()[0] for _ in range(m)]

    sl = sorted(sl)
    ans = 0
    for k in kl:
        ac = 0
        wa = n
        while ac + 1 < wa:
            wj = (ac + wa) // 2
            if k >= sl[wj]:
                ac = wj
            else:
                wa = wj

        if abs(sl[wa] - k) > abs(sl[ac] - k):
            c = abs(sl[ac] - k)
        else:
            c = abs(sl[wa] - k)

        ans += c

    print(ans)


if __name__ == '__main__':
    main()
