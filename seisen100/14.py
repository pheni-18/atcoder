# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b

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

    n, k = inp()
    al = inp()

    ans = float('inf')
    for _bit in product((1, 0), repeat=n):
        if not sum(_bit) == k:
            continue

        l = list(al)
        h = 0

        tot = 0
        for i in range(n):
            if _bit[i]:
                if l[i] > h:
                    h = l[i]
                    continue

                cost = h - l[i] + 1
                h += 1
                tot += cost
            else:
                h = max(h, l[i])

        ans = min(ans, tot)

    print(ans)


if __name__ == '__main__':
    main()
