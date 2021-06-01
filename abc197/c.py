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
    from itertools import product

    n = inp(True)
    al = inp(True)
    if type(al) == int:
        al = [al]

    ans = 2 ** 30 + 1

    for _bit in product((True, False), repeat=n - 1):
        bit = list(_bit) + [True]
        xo = 0
        o = 0
        for i in range(n):
            o |= al[i]
            if bit[i]:
                xo ^= o
                o = 0

        if xo < ans:
            ans = xo

    print(ans)


if __name__ == '__main__':
    main()
