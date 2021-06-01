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
    stl = inps(n, False)

    stl = [[st[0], int(st[1])] for st in stl]

    stl = sorted(stl, key=lambda x: x[1])

    print(stl[-2][0])


if __name__ == '__main__':
    main()
