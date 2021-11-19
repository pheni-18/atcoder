# https://atcoder.jp/contests/abc034/tasks/abc034_c

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


def main():
    W, H = inp()

    MOD = 10 ** 9 + 7

    a = 1
    b = 1
    c = 1
    for i in range(1, W + H - 2 + 1):
        a *= i
        a %= MOD
        if i <= H - 1:
            b *= i
            b %= MOD
        if i <= W - 1:
            c *= i
            c %= MOD

    ans = a * pow(b, MOD - 2, MOD)
    ans %= MOD
    ans *= pow(c, MOD - 2, MOD)
    ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
