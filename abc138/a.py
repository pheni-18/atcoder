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
    a = inp()[0]
    s = inp(False)[0]
    if a >= 3200:
        print(s)
    else:
        print('red')


if __name__ == '__main__':
    main()
