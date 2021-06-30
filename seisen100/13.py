# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e

# bit全探索


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

    r, c = inp()
    all_ = [inp() for _ in range(r)]

    ans = 0
    for _bit in product((True, False), repeat=r):
        r_all = []
        for i in range(r):
            if _bit[i]:
                r_al = list(map(lambda x: abs(x - 1), all_[i]))
                r_all.append(r_al)
            else:
                r_all.append(all_[i])

        tot = 0
        for i in range(c):
            s = 0
            for j in range(r):
                s += r_all[j][i]

            tot += max((r - s), s)

        ans = max(ans, tot)

    print(ans)


if __name__ == '__main__':
    main()
