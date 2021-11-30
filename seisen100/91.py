# https://atcoder.jp/contests/abc144/tasks/abc144_d

# 幾何計算


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inp_one(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    s = input()
    return int(s) if to_int else s


def main():
    import math

    a, b, x = inp()

    s = x / a
    if s > a * b / 2:
        h = (a * b - s) * 2 / a
        r = math.atan2(h, a)
    else:
        w = 2 * s / b
        r = math.atan2(b, w)

    ans = r / (2 * math.pi) * 360
    print(ans)


if __name__ == '__main__':
    main()
