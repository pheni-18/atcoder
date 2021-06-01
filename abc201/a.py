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
    al = inp()

    al = sorted(al)
    a1, a2, a3 = al
    if a3 - a2 == a2 - a1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
