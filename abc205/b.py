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
    al = inp()

    al = sorted(al)

    l = []
    for i in range(1, n + 1):
        l.append(i)

    if al == l:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
