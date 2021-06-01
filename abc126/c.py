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
    from decimal import Decimal
    n, k = inp()

    ans = Decimal(0)
    for i in range(1, n + 1):
        if i >= k:
            ans += Decimal(1) / Decimal(n)
            continue
        w = 1
        for j in range(1, 18):
            w *= 2
            if i * (2 ** j) >= k:
                ans += Decimal(1) / (Decimal(n) * Decimal(w))
                break

    print(ans)


if __name__ == '__main__':
    main()
