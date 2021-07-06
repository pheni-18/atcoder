# https://atcoder.jp/contests/abc077/tasks/arc084_a

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
    al = inp()
    bl = inp()
    cl = inp()

    bl.append(0)
    bl.append(1001001001)
    bl = sorted(bl)

    cl.append(0)
    cl.append(1001001001)
    cl = sorted(cl)

    cnt_bl = [0]
    for i in reversed(range(1, n + 1)):
        b = bl[i]
        ac = n + 1
        wa = 0
        while wa + 1 < ac:
            wj = (wa + ac) // 2
            if b < cl[wj]:
                ac = wj
            else:
                wa = wj

        cnt = n + 1 - ac
        cnt_bl.append(cnt_bl[-1] + cnt)

    cnt_bl.append(0)
    cnt_bl = list(reversed(cnt_bl))

    ans = 0
    for a in al:
        ac = n + 1
        wa = 0
        while wa + 1 < ac:
            wj = (wa + ac) // 2
            if a < bl[wj]:
                ac = wj
            else:
                wa = wj

        ans += cnt_bl[ac]

    print(ans)


if __name__ == '__main__':
    main()
