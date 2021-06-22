# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja

# [二分探索]

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
    from itertools import product

    n = inp()[0]
    al = inp()
    q = inp()[0]
    ml = inp()

    tott = [False] * 2001

    for _bit in product((True, False), repeat=n):
        bit = list(_bit)
        tot = 0
        for i in range(n):
            if bit[i]:
                tot += al[i]

        if 1 <= tot <= 2000:
            tott[tot] = True

    for m in ml:
        if tott[m]:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    main()
