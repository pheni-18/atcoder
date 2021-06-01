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
    n, k = inp()
    s = inp(False)[0]

    sl = list(s)
    sl[k - 1] = sl[k - 1].lower()

    print(''.join(sl))

if __name__ == '__main__':
    main()
