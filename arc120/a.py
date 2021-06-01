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

    m = -1
    x = 0
    total = 0
    for i in range(n):
        if al[i] > m:
            m = al[i]

        x += al[i]
        total += x

        k = i + 1
        ans = (k * m) + total

        print(ans)


if __name__ == '__main__':
    main()
