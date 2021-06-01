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
    n = inp(False)[0]
    l = list(map(lambda x: int(x), list(n)))
    ml = list(map(lambda x: x % 3, l))

    total = sum(l)
    if total % 3 == 0:
        print(0)
        return

    if len(l) == 1:
        print(-1)
        return

    if total % 3 == 1:
        if 1 in ml:
            print(1)
            return

        if ml.count(2) >= 2 and len(ml) > 2:
            print(2)
            return

    if total % 3 == 2:
        if 2 in ml:
            print(1)
            return

        if ml.count(1) >= 2 and len(ml) > 2:
            print(2)
            return

    print(-1)


if __name__ == '__main__':
    main()
