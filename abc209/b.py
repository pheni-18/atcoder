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
    n, x = inp()
    al = inp()

    for i in range(n):
        if i % 2 == 1:
            al[i] -= 1

    if x >= sum(al):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
