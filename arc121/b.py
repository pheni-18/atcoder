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
    def f(l1, l2):
        l2 = sorted(l2)

        ans = 1001001001001001
        for x in l1:
            ac = 0
            wa = len(l2)

            while ac < wa - 1:
                i = (wa - ac) // 2
                if l2[i] >= x:
                    wa = i
                else:
                    ac = i

            l3 = []
            if len(l2) == 1:
                l3 = [abs(l2[0] - x)]
            else:
                l3 = [abs(l2[ac] - x), abs(l2[wa] - x)]
            res = min(l3)
            if res < ans:
                ans = res

            if ans == 0:
                return 0

        return ans

    n = inp()[0]
    rs = []
    gs = []
    bs = []
    for i in range(2 * n):
        a, c = inp(False)
        a = int(a)
        if c == 'R':
            rs.append(a)
        elif c == 'G':
            gs.append(a)
        elif c == 'B':
            bs.append(a)

    rm = len(rs) % 2
    gm = len(gs) % 2
    bm = len(bs) % 2

    if rm == 0 and gm == 0 and bm == 0:
        print(0)
        return

    if rm == 1 and gm == 1:
        ans = f(rs, gs)
        print(ans)
    elif rm == 1 and bm == 1:
        ans = f(rs, bs)
        print(ans)
    elif gm == 1 and bm == 1:
        ans = f(gs, bs)
        print(ans)


if __name__ == '__main__':
    main()
