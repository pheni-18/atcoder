# https://atcoder.jp/contests/abc128/tasks/abc128_c

# [bit全探索]


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

    n, m = inp()
    sll = []
    for i in range(m):
        l = inp()
        sll.append(l[1:])

    pl = inp()

    ans = 0
    for _bit in product((True, False), repeat=n):
        bit = list(_bit)
        for i in range(m):
            tot = 0
            for s in sll[i]:
                cur = s - 1
                if bit[cur]:
                    tot += 1
            if tot % 2 != pl[i]:
                break
        else:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
