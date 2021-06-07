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
    x, y = inp()
    if x == y:
        print(x)
    elif x == 0 and y == 1:
        print(2)
    elif x == 1 and y == 0:
        print(2)
    elif x == 1 and y == 2:
        print(0)
    elif x == 2 and y == 1:
        print(0)
    elif x == 0 and y == 2:
        print(1)
    elif x == 2 and y == 0:
        print(1)


if __name__ == '__main__':
    main()
