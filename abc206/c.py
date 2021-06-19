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

    d = {}
    for i in range(n):
        if al[i] in d:
            d[al[i]] += 1
        else:
            d[al[i]] = 1

    c = (n * (n - 1)) // 2
    ans = c
    for v in d.values():
        if v >= 2:
            ans -= (v * (v - 1)) // 2

    print(ans)


if __name__ == '__main__':
    main()
