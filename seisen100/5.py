# https://atcoder.jp/contests/abc095/tasks/arc096_ahttps://atcoder.jp/contests/abc095/tasks/arc096_a


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
    a, b, c, x, y = inp()

    ans = float('inf')
    n = max(x, y)
    for i in range((2 * n) + 1):
        tot = i * c

        sa_x = (x - (i // 2))
        if sa_x > 0:
            tot += sa_x * a

        sa_y = (y - (i // 2))
        if sa_y > 0:
            tot += sa_y * b

        ans = min(ans, tot)

    print(ans)


if __name__ == '__main__':
    main()
