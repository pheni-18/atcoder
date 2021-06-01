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
    t, n = inp()

    x = ((100 / t) * n) + n
    if 100 % t == 0:
        x = int(x) - 1
    else:
        x = int(x)

    print(x)


if __name__ == '__main__':
    main()
