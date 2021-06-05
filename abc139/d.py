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

    x = n // 2
    if n % 2 == 0:
        y = 2 * x
        ans = y * (x - 1) + x
    else:
        y = (2 * x) + 1
        ans = y * x

    print(ans)


if __name__ == '__main__':
    main()
