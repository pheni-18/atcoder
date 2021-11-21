# https://atcoder.jp/contests/abc021/tasks/abc021_d

# 逆元


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


def cmb(n, r, mod):
    a, b, c = 1, 1, 1
    for i in range(1, n + 1):
        a *= i
        a %= mod
        if i <= n - r:
            b *= i
            b %= mod
        if i <= r:
            c *= i
            c %= mod

    res = a * pow(b, mod - 2, mod)
    res %= mod
    res *= pow(c, mod - 2, mod)
    res %= mod
    return res


def main():
    n = inp_one()
    k = inp_one()

    MOD = 10 ** 9 + 7

    ans = cmb(n + k - 1, k, MOD)
    print(ans)


if __name__ == '__main__':
    main()
