# https://atcoder.jp/contests/arc054/tasks/arc054_b

# 二分探索


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

    p = float(input())

    def f(x):
        return x + p / (2 ** (x / 1.5))

    def fd(x):
        return 1 + p * math.log(2 ** (-1 / 1.5)) * (2 ** (-x / 1.5))

    left = 0
    right = p
    for _ in range(1000):
        wj = (left + right) / 2
        if fd(wj) >= 0:
            right = wj
        else:
            left = wj

    print(f(wj))


if __name__ == '__main__':
    main()
