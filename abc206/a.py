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
    import math
    n = inp()[0]
    v = math.floor(n * 1.08)
    if v > 206:
        print(':(')
    elif v == 206:
        print('so-so')
    else:
        print('Yay!')


if __name__ == '__main__':
    main()
