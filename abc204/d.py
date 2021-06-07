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
    tl = inp()

    sorted_tl = sorted(tl, reverse=True)

    a = sorted_tl[0]
    b = 0
    for i in range(1, n):
        if a > b:
            b += sorted_tl[i]
        else:
            a += sorted_tl[i]

    print(max(a, b))



if __name__ == '__main__':
    main()
