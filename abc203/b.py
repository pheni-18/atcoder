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
    n, k = inp()

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            x = str(i) + '0' + str(j)
            ans += int(x)

    print(ans)


if __name__ == '__main__':
    main()
