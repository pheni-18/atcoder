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
    vl = inp()

    for _ in range(n - 1):
        vl = sorted(vl)
        vl.append((vl[0] + vl[1]) / 2)
        vl.pop(0)
        vl.pop(0)

    print(vl[0])


if __name__ == '__main__':
    main()
