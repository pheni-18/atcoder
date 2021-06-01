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


    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n = inp()[0]
    al = inp()
    ans = 0
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if (al[i] - al[j]) % 200 == 0:
    #             ans += 1

    ml = [0] * 200
    for a in al:
        i = a % 200
        ml[i] += 1

    for m in ml:
        if m >= 2:
            ans += combinations_count(m, 2)

    print(ans)


if __name__ == '__main__':
    main()
