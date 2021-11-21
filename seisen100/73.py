# https://atcoder.jp/contests/abc145/tasks/abc145_d

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
    X, Y = inp()

    MOD = 10 ** 9 + 7

    for a in range(X + 1):
        if (X - a) % 2 == 1:
            continue

        b = (X - a) // 2
        if 2 * a + b == Y:
            break
    else:
        print(0)
        return

    ans = cmb(a + b, a, MOD)
    print(ans)


if __name__ == '__main__':
    main()
