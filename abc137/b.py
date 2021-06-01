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
    k, x = inp()

    le = x - (k - 1)
    ri = x + (k - 1)

    ansl = []
    for i in range(le, ri + 1):
        ansl.append(str(i))

    print(' '.join(ansl))


if __name__ == '__main__':
    main()
